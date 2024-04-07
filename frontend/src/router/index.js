import { createWebHistory, createRouter } from "vue-router";

import assignemntPreview from "@/views/AssignmentPreview.vue";
import linkOfAssignments from "@/views/ListOfAssignments.vue";
import submitForm from "@/views/SubmitForm.vue";
import listOfStudents from "@/views/ListOfStudents.vue";
import user from "@/views/UserProfile.vue";
import main from "@/views/MainScreen.vue";
import student from "@/views/StudentPreview.vue";



const routes = [
  {
    path: "/",
    name: "main",
    component: main,
  },
  {
    path: "/assignemntPreview",
    name: "assignemntPreview",
    component: assignemntPreview,
  },
  {
    path: "/linkOfAssignments",
    name: "linkOfAssignments",
    component: linkOfAssignments,
  },
  {
    path: "/listOfStudents",
    name: "listOfStudents",
    component: listOfStudents,
  },
  {
    path: "/form",
    name: "submitForm",
    component: submitForm,
  },
  {
    path: "/user",
    name: "user",
    component: user,
  }
  ,
  {
    path: "/student/:id",
    name: "student",
    component: student,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
