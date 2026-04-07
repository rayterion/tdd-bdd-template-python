# Factory Boy & Faker — Complete Guide

This guide covers everything you need to generate realistic test data using **factory_boy** and **Faker** in a Python/pytest project.

---

## Table of Contents

1. [What Are These Libraries?](#1-what-are-these-libraries)
2. [Installation](#2-installation)
3. [Faker Basics](#3-faker-basics)
4. [Factory Boy Basics](#4-factory-boy-basics)
5. [Connecting Faker to Factory Boy](#5-connecting-faker-to-factory-boy)
6. [Relationships Between Factories](#6-relationships-between-factories)
7. [Traits and Lazy Attributes](#7-traits-and-lazy-attributes)
8. [Sequences](#8-sequences)
9. [Overriding Values at Call Time](#9-overriding-values-at-call-time)
10. [Factory Strategies: build vs create vs stub](#10-factory-strategies-build-vs-create-vs-stub)
11. [Using Factories in Pytest](#11-using-factories-in-pytest)
12. [Common Faker Providers Cheat Sheet](#12-common-faker-providers-cheat-sheet)
13. [Tips & Best Practices](#13-tips--best-practices)

---

## 1. What Are These Libraries?

| Library | Purpose |
|---|---|
| **Faker** | Generates realistic fake data (names, emails, addresses, dates, …) |
| **factory_boy** | Creates object instances (plain Python, Django models, SQLAlchemy, …) with sensible defaults, using Faker under the hood |

Together they let you create fully populated test objects in one line instead of hand-crafting dictionaries everywhere.

---

## 2. Installation

Both packages are already in this project's `requirements.txt`. Install into the virtual environment:

```bash
# Windows — activate the project venv first
.venv\Scripts\activate

pip install factory_boy Faker
```

Verify:

```bash
python -c "import factory, faker; print(factory.__version__, faker.__version__)"
```

---

## 3. Faker Basics

`Faker` is a standalone library. You can use it directly without factory_boy.

```python
from faker import Faker

fake = Faker()

# Basic providers
print(fake.name())           # e.g. "Laura Schmidt"
print(fake.email())          # e.g. "user@example.com"
print(fake.address())        # multi-line address string
print(fake.phone_number())   # locale-aware phone number
print(fake.date_of_birth())  # datetime.date object
print(fake.text(max_nb_chars=100))  # lorem-style paragraph

# Numbers
print(fake.random_int(min=1, max=100))
print(fake.pyfloat(left_digits=2, right_digits=2, positive=True))

# UUIDs
print(fake.uuid4())
```

### Locales

```python
fake_br = Faker("pt_BR")
fake_de = Faker("de_DE")
fake_jp = Faker("ja_JP")

print(fake_br.name())   # Brazilian Portuguese name
print(fake_de.city())   # German city
```

### Seeding for Reproducibility

```python
Faker.seed(42)
fake = Faker()
print(fake.name())  # same value every run
```

---

## 4. Factory Boy Basics

factory_boy creates **factory classes** tied to a Python class (your model or dataclass). Each field maps to a declaration that produces a default value.

### With a plain Python class

```python
# src/core/models.py  (simplified example)
class User:
    def __init__(self, id, username, email, is_active=True):
        self.id = id
        self.username = username
        self.email = email
        self.is_active = is_active
```

```python
# src/tests/factories.py
import factory

class UserFactory(factory.Factory):
    class Meta:
        model = User          # the class to instantiate

    id       = factory.Sequence(lambda n: n)
    username = factory.Faker("user_name")
    email    = factory.Faker("email")
    is_active = True
```

### Building an instance

```python
user = UserFactory()
print(user.username)   # a random username
print(user.email)      # a random email

# Build many at once
users = UserFactory.create_batch(5)
```

---

## 5. Connecting Faker to Factory Boy

`factory.Faker` wraps any **Faker provider** directly inside a factory declaration.

```python
import factory

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name        = factory.Faker("word")
    description = factory.Faker("sentence", nb_words=10)
    price       = factory.Faker("pyfloat", left_digits=3, right_digits=2, positive=True)
    sku         = factory.Faker("ean13")        # 13-digit barcode string
    created_at  = factory.Faker("date_this_decade")
```

Pass any keyword argument that the Faker provider accepts directly after the provider name.

### Setting a global locale

```python
factory.Faker._DEFAULT_LOCALE = "pt_BR"
```

Or per-field:

```python
name = factory.Faker("name", locale="ja_JP")
```

---

## 6. Relationships Between Factories

### SubFactory — one-to-one / many-to-one

```python
class AddressFactory(factory.Factory):
    class Meta:
        model = Address

    street = factory.Faker("street_address")
    city   = factory.Faker("city")
    country = factory.Faker("country_code")


class UserFactory(factory.Factory):
    class Meta:
        model = User

    name    = factory.Faker("name")
    address = factory.SubFactory(AddressFactory)
```

`user.address` is a fully built `Address` instance.

### RelatedFactory — reverse / one-to-many

```python
class CompanyFactory(factory.Factory):
    class Meta:
        model = Company

    name  = factory.Faker("company")
    # Create 3 employees after the company is built
    employees = factory.RelatedFactory(
        UserFactory, factory_related_name="employer", size=3
    )
```

---

## 7. Traits and Lazy Attributes

### Traits — named variations of a factory

```python
class UserFactory(factory.Factory):
    class Meta:
        model = User

    username  = factory.Faker("user_name")
    is_active = True
    is_admin  = False

    class Params:
        admin = factory.Trait(is_active=True, is_admin=True)
        inactive = factory.Trait(is_active=False)

# Usage
admin_user    = UserFactory(admin=True)
inactive_user = UserFactory(inactive=True)
```

### LazyAttribute — compute a field from other fields

```python
class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name  = factory.Faker("last_name")
    # email is derived from the generated first/last name
    email = factory.LazyAttribute(
        lambda obj: f"{obj.first_name.lower()}.{obj.last_name.lower()}@example.com"
    )
```

### LazyFunction — call any zero-argument callable

```python
import datetime

class EventFactory(factory.Factory):
    class Meta:
        model = Event

    name       = factory.Faker("catch_phrase")
    created_at = factory.LazyFunction(datetime.datetime.utcnow)
```

---

## 8. Sequences

`factory.Sequence` produces a unique, incrementing value per instance — perfect for IDs and unique usernames.

```python
class UserFactory(factory.Factory):
    class Meta:
        model = User

    id       = factory.Sequence(lambda n: n + 1)
    username = factory.Sequence(lambda n: f"user_{n:04d}")   # user_0001, user_0002 …
    email    = factory.Sequence(lambda n: f"user{n}@example.com")
```

Reset the counter between test runs if needed:

```python
UserFactory.reset_sequence(0)
```

---

## 9. Overriding Values at Call Time

Every field can be overridden when you build an instance:

```python
# Override one field
user = UserFactory(email="fixed@example.com")

# Override a nested SubFactory field using double-underscore
user = UserFactory(address__city="São Paulo")

# Override multiple fields at once
user = UserFactory(
    username="alice",
    is_active=False,
    address__country="BR",
)
```

---

## 10. Factory Strategies: build vs create vs stub

| Method | What it does |
|---|---|
| `Factory.build()` | Constructs the object **without** saving it (calls `__init__` only) |
| `Factory.create()` | Constructs **and** saves it (calls `_create` hook — used with ORMs) |
| `Factory.stub()` | Returns a lightweight `StubObject` with attributes set but no real class |
| `Factory.build_batch(n)` | Returns a list of `n` built objects |
| `Factory.create_batch(n)` | Returns a list of `n` created objects |

For plain Python classes (no ORM), `build` and `create` behave identically.

When using **Django** or **SQLAlchemy**, swap the base class:

```python
# Django
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "myapp.User"  # or the model class directly

# SQLAlchemy
class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session
```

---

## 11. Using Factories in Pytest

### Direct usage in a test

```python
from src.tests.factories import UserFactory

def test_user_is_active_by_default():
    user = UserFactory()
    assert user.is_active is True

def test_admin_user_has_admin_flag():
    admin = UserFactory(admin=True)
    assert admin.is_admin is True
```

### Sharing factories via fixtures

```python
# src/tests/conftest.py
import pytest
from src.tests.factories import UserFactory

@pytest.fixture
def default_user():
    return UserFactory()

@pytest.fixture
def admin_user():
    return UserFactory(admin=True)
```

```python
# src/tests/unit/test_user.py
def test_default_user_fixture(default_user):
    assert default_user.is_active is True

def test_admin_fixture(admin_user):
    assert admin_user.is_admin is True
```

### Parametrize with factories

```python
import pytest
from src.tests.factories import UserFactory

@pytest.mark.parametrize("is_active", [True, False])
def test_user_status(is_active):
    user = UserFactory(is_active=is_active)
    assert user.is_active == is_active
```

---

## 12. Common Faker Providers Cheat Sheet

```python
from faker import Faker
fake = Faker()

# Person
fake.name()            # "John Doe"
fake.first_name()      # "John"
fake.last_name()       # "Doe"
fake.prefix()          # "Dr."
fake.suffix()          # "Jr."

# Internet
fake.email()           # "user@example.com"
fake.user_name()       # "john_doe42"
fake.url()             # "https://example.com/path"
fake.ipv4()            # "192.168.1.1"
fake.ipv6()            # full IPv6 string
fake.domain_name()     # "example.org"
fake.slug()            # "some-random-slug"

# Address
fake.address()         # full multi-line address
fake.street_address()  # "123 Main St"
fake.city()            # "Springfield"
fake.state()           # "Texas"
fake.country()         # "Brazil"
fake.country_code()    # "BR"
fake.postcode()        # "12345"
fake.latitude()        # Decimal("-34.6")
fake.longitude()       # Decimal("-58.3")

# Date & Time
fake.date()                        # "2024-03-15"
fake.date_of_birth(minimum_age=18) # datetime.date
fake.date_time_this_year()         # datetime.datetime
fake.time()                        # "14:30:00"
fake.timezone()                    # "America/Sao_Paulo"
fake.unix_time()                   # int timestamp

# Numbers
fake.random_int(min=0, max=100)
fake.random_digit()                # 0–9
fake.pyfloat(positive=True, left_digits=3, right_digits=2)
fake.numerify("###-###")           # "482-971"

# Text
fake.word()            # "apple"
fake.words(5)          # ["apple", "blue", ...]
fake.sentence()        # "The quick brown fox."
fake.paragraph()       # multi-sentence paragraph
fake.text(200)         # ~200 chars of lorem text
fake.bs()              # business jargon: "synergize vertical markets"
fake.catch_phrase()    # "Optional contextually-based website"
fake.job()             # "Software Engineer"

# Finance
fake.credit_card_number()  # "4111111111111111"
fake.currency_code()       # "BRL"
fake.pricetag()            # "$12.99"

# Misc
fake.uuid4()               # UUID string
fake.color_name()          # "Coral"
fake.hex_color()           # "#a3c2d4"
fake.boolean()             # True / False
fake.md5()                 # 32-char hex string
fake.sha256()              # 64-char hex string
fake.ean13()               # 13-digit barcode string
fake.isbn13()              # "978-3-16-148410-0"
```

---

## 13. Tips & Best Practices

1. **Keep factories next to tests** — place them in `src/tests/factories.py` or a `factories/` sub-package so they are easy to find.
2. **Don't over-fake** — only generate values that vary per scenario; hardcode truly fixed business rules.
3. **Use `build()` for unit tests** — no persistence overhead; use `create()` only when the database state matters.
4. **Seed Faker in CI** — call `Faker.seed(0)` in a session-scoped fixture to get deterministic failures that are reproducible.
5. **Reset sequences per test** — add `UserFactory.reset_sequence()` inside a fixture to prevent leakage between tests.
6. **Traits over subclassing** — prefer `Params` traits for variations rather than creating `AdminUserFactory`, `InactiveUserFactory`, etc.
7. **Combine LazyAttribute with Faker** — derive related fields (e.g. email from name) to keep data internally consistent.
8. **Use `factory.Faker` locale parameter sparingly** — set a global default instead of per-field overrides to avoid confusion.

---

## Quick Reference

```bash
# Install
pip install factory_boy Faker

# Build a single object (no persistence)
obj = MyFactory.build()

# Build with overrides
obj = MyFactory.build(field="value", nested__field="value")

# Build a list
objs = MyFactory.build_batch(10)

# Activate a trait
obj = MyFactory(my_trait=True)

# Reset sequence counter
MyFactory.reset_sequence(0)
```
