# Exercise: Accessing Custom Fields

1. Open shell_plus on your CloudBolt instance if it's not already open
2. Get a reference to the last Server added to your CloudBolt instance:
    * `s = Server.objects.last()`↵
3. List the Custom Field Values (CFVs) attached to this server: 
    * `list(s.custom_field_values.all())`↵
4. List the Custom Field name and value for each CFV:
    * `[f"{cfv.field.name}={cfv.value}" for cfv in s.custom_field_values.all()]`↵
5. Use auto-complete to access Custom Fields directly:
    * Type `s.ti`⇥
    * Type `s.sc`⇥
    * Note these autocomplete to the name of the Custom Field.
    * Also note, these Custom Fields are dynamic, therefore they are not listed in Model documentation

