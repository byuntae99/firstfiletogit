from django.urls import path, include
from . import views



urlpatterns = [
    ###___ADMIN___###
    path('', views.loginPage, name="login"),         
    path('doLogin/', views.doLogin, name="doLogin"),
    #path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('admin_home/', views.adminhome, name="admin_home"),
    path('add_student/', views.addstudent, name="add_student"),
    path('add_student_save/', views.addstudentsave, name="add_student_save"),
    path('edit_student/<student_id>', views.editstudent, name="edit_student"),
    path('edit_student_save/', views.edit_student_save, name="edit_student_save"),
    path('manage_student/', views.managestudent, name="manage_student"),
    path('delete_student/<student_id>/', views.deletestudent, name="delete_student"),
    path('check_email_exist/', views.checkemailexist, name="check_email_exist"),
    path('check_username_exist/', views.checkusernameexist, name="check_username_exist"),
    path('student_leave_view/', views.studentleaveview, name="student_leave_view"),
    path('student_leave_approve/<leave_id>/', views.studentleaveapprove, name="student_leave_approve"),
    path('student_leave_reject/<leave_id>/', views.studentleavereject, name="student_leave_reject"),
    path('course_reg_confirm/',views.course_reg_confirm,name="course_reg_confirm"),
    path('course_reg_update',views.course_reg_update,name="course_reg_update"),
    # URLS for ___Students___
    path('student_home/', views.studenthome, name="student_home"),
    path('student_apply_leave/', views.studentapplyleave, name="student_apply_leave"),
    path('student_apply_leave_save/', views.studentapplyleavesave, name="student_apply_leave_save"),
    path('cancel_leave',views.cancelleave,name="cancel_leave"),
    path('student_register/',views.student_register,name="student_register"),
    path('crssavwe/',views.crssavwe,name="crssavwe"),
    path('dowload_course_doc/',views.dowload_course_doc,name="dowload_course_doc"),
    
    ]
