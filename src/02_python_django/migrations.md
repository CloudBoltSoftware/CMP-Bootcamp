# Django Database Migrations

* Used to manage database changes to the underlying database in a Django project
* Migrations are created by tracking changes to Django ORM Model objects
* Each Django Application has its own set of database migrations
  * These migrations are checked into git as code
  * Applied by application
* Migrations can be run forward and backward, though moving backward can be very risky
* A ledger of applied migrations is stored in the managed database
* Since migrations are tracked in the database, it's ok to apply migrations to the same database multiple times.
  * This is important when upgrading HA environments.

## Some Useful Tips on Migrations
* ALWAYS backup/snapshot the database BEFORE running migrations/upgrades!
* Schema changes and data migrations should never co-exist in a single migration
* Migrations must be self-contained -- never import from the application
  * Rely on "frozen-in-time" methods in the migration itself.
* NEVER fake migrations in a customer environment -- almost never the right solution.






