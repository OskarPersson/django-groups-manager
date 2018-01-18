from django.conf.urls import url

from groups_manager import views

app_name = 'groups_manager'

urlpatterns = [

    url(r'^$',
        views.GroupsManagerView.as_view(),
        name='groups_manager',),

    url(r'^member/$',
        views.MemberListView.as_view(),
        name='member_list',),
    url(r'^member/add/$',
        views.MemberCreateView.as_view(),
        name='member_add',),
    url(r'^member/(?P<pk>\d+)/$',
        views.MemberDetailView.as_view(),
        name='member_detail',),
    url(r'^member/(?P<pk>\d+)/edit/$',
        views.MemberEditView.as_view(),
        name='member_edit',),
    url(r'^member/(?P<pk>\d+)/delete/$',
        views.MemberDeleteView.as_view(),
        name='member_delete',),

    url(r'^group-type/$',
        views.GroupTypeListView.as_view(),
        name='group_type_list',),
    url(r'^group-type/add/$',
        views.GroupTypeCreateView.as_view(),
        name='group_type_add',),
    url(r'^group-type/(?P<pk>\d+)/$',
        views.GroupTypeDetailView.as_view(),
        name='group_type_detail',),
    url(r'^group-type/(?P<pk>\d+)/edit/$',
        views.GroupTypeEditView.as_view(),
        name='group_type_edit',),
    url(r'^group-type/(?P<pk>\d+)/delete/$',
        views.GroupTypeDeleteView.as_view(),
        name='group_type_delete',),

    url(r'^group-entity/$',
        views.GroupEntityListView.as_view(),
        name='group_entity_list',),
    url(r'^group-entity/add/$',
        views.GroupEntityCreateView.as_view(),
        name='group_entity_add',),
    url(r'^group-entity/(?P<pk>\d+)/$',
        views.GroupEntityDetailView.as_view(),
        name='group_entity_detail',),
    url(r'^group-entity/(?P<pk>\d+)/edit/$',
        views.GroupEntityEditView.as_view(),
        name='group_entity_edit',),
    url(r'^group-entity/(?P<pk>\d+)/delete/$',
        views.GroupEntityDeleteView.as_view(),
        name='group_entity_delete',),

    url(r'^group/$',
        views.GroupListView.as_view(),
        name='group_list',),
    url(r'^group/add/$',
        views.GroupCreateView.as_view(),
        name='group_add',),
    url(r'^group/(?P<pk>\d+)/$',
        views.GroupDetailView.as_view(),
        name='group_detail',),
    url(r'^group/(?P<pk>\d+)/edit/$',
        views.GroupEditView.as_view(),
        name='group_edit',),
    url(r'^group/(?P<pk>\d+)/delete/$',
        views.GroupDeleteView.as_view(),
        name='group_delete',),

    url(r'^group-member-role/$',
        views.GroupMemberRoleListView.as_view(),
        name='group_member_role_list',),
    url(r'^group-member-role/add/$',
        views.GroupMemberRoleCreateView.as_view(),
        name='group_member_role_add',),
    url(r'^group-member-role/(?P<pk>\d+)/$',
        views.GroupMemberRoleDetailView.as_view(),
        name='group_member_role_detail',),
    url(r'^group-member-role/(?P<pk>\d+)/edit/$',
        views.GroupMemberRoleEditView.as_view(),
        name='group_member_role_edit',),
    url(r'^group-member-role/(?P<pk>\d+)/delete/$',
        views.GroupMemberRoleDeleteView.as_view(),
        name='group_member_role_delete',),

    url(r'^group-member/(?P<pk>\d+)/edit/$',
        views.GroupMemberEditView.as_view(),
        name='group_member_edit',),
    url(r'^group-member/(?P<pk>\d+)/delete/$',
        views.GroupMemberDeleteView.as_view(),
        name='group_member_delete',),
    url(r'^group-member/group/(?P<group_id>\d+)/add-member/$',
        views.GroupMemberAddMemberView.as_view(),
        name='group_member_add_member',),
    url(r'^group-member/member/(?P<member_id>\d+)/add-group/$',
        views.GroupMemberAddGroupView.as_view(),
        name='group_member_add_group',),

]
