from django.urls import path
import customers.views

urlpatterns = [    
    path("", customers.views.show_profiles,
         name="show_profiles_route"),
    path("create/", customers.views.create_profile,
         name="create_profile_route"),
    path("update/<profile_id>", customers.views.update_profile,
         name="update_profile_route"),
    path("delete/<profile_id>", customers.views.delete_profile,
         name="delete_profile_route"),
]


#   <!-- <ul>
#             {% for each_exercise in all_exercises %}
#             <li>
#                 {% cloudinary each_exercise.cover class="exercise_cover"%}
#                 <a href="{% url 'exercise_details_route' exercise_id=each_exercise.id %}">{{each_exercise.title}}</a> 
#                 <a class="btn btn-primary" href="{% url 'update_exercise_route' exercise_id=each_exercise.id%}">Edit</a>
#                 <a class="btn btn-danger" href="{% url 'delete_exercise_route' exercise_id=each_exercise.id%}">Delete</a>
#                 <a class="btn btn-dark" href="{% url 'add_to_exercise_cart_route' exercise_id=each_exercise.id%}">Add to Cart</a>
#             </li>
#         </ul> -->