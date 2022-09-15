# Exercise: Query and Update CloudBolt Objects

Let's open `shell_plus` on your CloudBolt instance…

## Learn More about Models
1. List the available fields on CloudBolt objects:
   * `Server._meta.fields` ↵
   * `Environment._meta.fields` ↵
   * `Group._meta.fields` ↵
2. List objects related to a given CloudBolt object:
   * `Server._meta.related_objects` ↵

## Update Model Attributes
1. Get a reference to the last Environment created:
   * `env = Environment.objects.last()` ↵
2. Update the name of the Environment:
   * `env.name = 'Data Center'` ↵
3. Don't forget to save!
   * `env.save()` ↵



