# Generated by Django 4.1.3 on 2023-06-02 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import network.validators


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='level2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intrest_name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='level3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intrest_name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Default', 'Default'), ('User_Fllow', 'User_Fllow'), ('User_Fllowing', 'User_Fllowing'), ('User_Post_like', 'User_Post_like'), ('User_New_Post', 'User_New_Post'), ('User_Post_Reviwes', 'User_Post_Reviwes'), ('User_Post_Reviwes_Replay', 'User_Post_Reviwes_Replay'), ('Page_Invitions_To_User', 'Page_Invitions_To_User'), ('User_Accept_userpage_Invitions', 'User_Accept_userpage_Invitions'), ('User_Accept_Page_Invitions', 'User_Accept_Page_Invitions'), ('User_Page_Join_Request', 'User_Page_Join_Request'), ('Page_Accept_User_Invitions', 'Page_Accept_User_Invitions'), ('Page_New_Post', 'Page_New_Post'), ('Page_Post_like', 'User_Post_like'), ('Page_Post_Reviwes', 'Page_Post_Reviwes'), ('Page_Post_Reviwes_Replay', 'Page_Post_Reviwes_Replay'), ('Intrest_Post_Reviwes', 'Intrest_Post_Reviwes'), ('Intrest_Post_Reviwes_Replay', 'Intrest_Post_Reviwes_Replay'), ('Intrest_level_2_Post_Reviwes', 'Intrest_level_2_Post_Reviwes'), ('Intrest_level_2_Post_Reviwes_Replay', 'Intrest_level_2_Post_Reviwes_Replay')], default='Default', max_length=150)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_read', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Order_Itemz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Orderz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=255, null=True)),
                ('Phone', models.CharField(max_length=12, null=True)),
                ('House', models.CharField(max_length=255, null=True)),
                ('Area', models.CharField(max_length=60, null=True)),
                ('Landmark', models.CharField(max_length=60, null=True)),
                ('Town', models.CharField(max_length=60, null=True)),
                ('State', models.CharField(max_length=60, null=True)),
                ('Zip', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='pagefollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.TextField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='post_viewers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PostViewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewz', models.CharField(blank=True, max_length=255, null=True)),
                ('mail', models.EmailField(blank=True, max_length=255, null=True)),
                ('rating', models.IntegerField(blank=True, max_length=255, null=True)),
                ('review_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_text', models.CharField(max_length=255)),
                ('reply_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='viewers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='order_item',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order_item',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order_item',
            name='user',
        ),
        migrations.RemoveField(
            model_name='shipping_address',
            name='user',
        ),
        migrations.RemoveField(
            model_name='invite_request',
            name='stat',
        ),
        migrations.RemoveField(
            model_name='post',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tages_n',
        ),
        migrations.RemoveField(
            model_name='post',
            name='vedio',
        ),
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
        migrations.AddField(
            model_name='friend_request',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='intrest',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intrest',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.intrest'),
        ),
        migrations.AddField(
            model_name='intrest',
            name='tooltip',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='intrest',
            name='tooltip2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='invite_request',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='invite_request',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('User_Pending', 'User_Pending'), ('Joined', 'Joined'), ('Rejected', 'Rejected')], default='Pending', max_length=150),
        ),
        migrations.AddField(
            model_name='page',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='education',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='facebook_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='linkedin_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='mobile',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='twitter_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='website_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='you_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Offer_End_Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Offer_Start_Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Offer_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Offer_toggle',
            field=models.CharField(default='Normal', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='average_rating',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='intr_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='network.intrest'),
        ),
        migrations.AddField(
            model_name='post',
            name='views_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='education',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='genter',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='website_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='you_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Product_Price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content_image',
            field=models.FileField(blank=True, null=True, upload_to='posts/', validators=[network.validators.file_size]),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Order_Item',
        ),
        migrations.DeleteModel(
            name='Shipping_address',
        ),
        migrations.AddField(
            model_name='viewers',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewed_post', to='network.post'),
        ),
        migrations.AddField(
            model_name='viewers',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewed_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewreply',
            name='replier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reviewreply',
            name='reviews',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='network.review'),
        ),
        migrations.AddField(
            model_name='review',
            name='post',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewposst', to='network.post'),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postviewer',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.post'),
        ),
        migrations.AddField(
            model_name='postviewer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post_viewers',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_viewed', to='network.post'),
        ),
        migrations.AddField(
            model_name='post_viewers',
            name='viewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_viewed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pagefollow',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pagefollow',
            name='to_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_page', to='network.page'),
        ),
        migrations.AddField(
            model_name='orderz',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order_itemz',
            name='free_download_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order_itemz',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='network.orderz'),
        ),
        migrations.AddField(
            model_name='order_itemz',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network.post'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='ReviewReply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ReviewReply', to='network.reviewreply'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='friend_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friend_request', to='network.friend_request'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='from_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fr_noti', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notifications',
            name='invite_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invite_request', to='network.invite_request'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='pages',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pagz_noti', to='network.page'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_noti', to='network.post'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='network.review'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='to_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_noti', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='level3',
            name='parent_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='network.intrest'),
        ),
        migrations.AddField(
            model_name='level3',
            name='parent_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='network.level2'),
        ),
        migrations.AddField(
            model_name='level2',
            name='parent_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='network.intrest'),
        ),
        migrations.AddField(
            model_name='download',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downloading_post', to='network.post'),
        ),
        migrations.AddField(
            model_name='download',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downloading_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='lev2_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='network.level2'),
        ),
    ]