# Generated by Django 2.2.7 on 2019-12-03 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='MealCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('departmentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_categories', to='food.Departments', verbose_name='DemartmentID')),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('description', models.TextField(verbose_name='Description')),
                ('categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Meals', to='food.MealCategories', verbose_name='CategoryID')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='ServicePercentage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.IntegerField(verbose_name='Percentage')),
            ],
        ),
        migrations.CreateModel(
            name='Statuses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('to do', 'to do'), ('in progress', 'in progress'), ('done', 'done')], max_length=30, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Tables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('login', models.CharField(max_length=50, verbose_name='Login')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('dateofadd', models.DateField()),
                ('phone', models.CharField(max_length=50)),
                ('roleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Users', to='food.Roles', verbose_name='RoleID')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tablename', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Number of table')),
                ('isitopen', models.BooleanField()),
                ('date', models.DateField()),
                ('mealsid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Orders', to='food.Meals', verbose_name='Meal')),
                ('tableid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Orders', to='food.Tables', verbose_name='Table')),
                ('waiterid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Orders', to='food.Users', verbose_name='Waiter')),
            ],
        ),
        migrations.CreateModel(
            name='GetUserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100)),
                ('roleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GetUserToken', to='food.Roles', verbose_name='RoleID')),
            ],
        ),
        migrations.CreateModel(
            name='Checks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('totalsum', models.IntegerField()),
                ('meals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Checks', to='food.Meals')),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Checks', to='food.Orders', verbose_name='Order')),
                ('servicefee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Checks', to='food.ServicePercentage')),
            ],
        ),
    ]