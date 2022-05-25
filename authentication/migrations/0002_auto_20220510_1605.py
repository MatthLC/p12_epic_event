from django.db import migrations


def create_groups(apps, schema_migration):
    User = apps.get_model('authentication', 'User')
    Group = apps.get_model('auth', 'Group')

    managers = Group(name='MANAGER')
    managers.save()

    sellers = Group(name='SALES')
    sellers.save()

    support = Group(name='SUPPORT')
    support.save()

    unknown = Group(name='UNKNOWN')
    unknown.save()

    for user in User.objects.all():
        if user.role == 'MANAGER':
            managers.user_set.add(user)
        if user.role == 'SALES':
            sellers.user_set.add(user)
        if user.role == 'SUPPORT':
            support.user_set.add(user)
        if user.role == 'NA':
            unknown.user_set.add(user)


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups)
    ]
