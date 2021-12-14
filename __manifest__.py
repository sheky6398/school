{
    "name":"School",
    "author":"Bharat yadav",
    "version":"1.3",
    "summary":"Students,Teachers, Courses, Subjects, and Fee of  School",
    "depends":['base','mail','product','sale','website'],
    "data":[  
        "security/security.xml",
        "security/ir.model.access.csv",      
        "wizard/register_payment_wizard_views.xml",                       
        "report/school_student_report.xml",
        "report/school_student_profile.xml",
        "data/student_mail_template.xml",
        "views/school_student_views.xml",
        "views/website_form.xml",
        "wizard/teacher_terminate_wizard_views.xml", 
        "report/school_teacher_profile.xml",
        "report/school_teacher_report.xml",
        "data/teacher_mail_template.xml",
        "views/school_teacher_views.xml",
        "views/school_course_views.xml",
        "views/school_student_fee_views.xml",
        "views/school_subject_views.xml",
        "views/res_partner_inherited_views.xml",
        "views/school_product_views.xml",
        "views/sale_order_views.xml",

    ],
    "demo":[
        "demo/course_demo.xml",
        "demo/student_demo.xml",
        "demo/teacher_demo.xml",
        "demo/subject_demo.xml" 
    ]
}