import { createWebHistory, createRouter } from "vue-router";
import LoginPage from "@/views/LoginPage.vue";
import assignemntPreview from "@/views/AssignmentPreview.vue";
import linkOfAssignments from "@/views/ListOfAssignments.vue";
import submitForm from "@/views/SubmitForm.vue";
import listOfStudents from "@/views/ListOfStudents.vue";



const routes = [
  {
    path: "/",
    name: "LoginPage",
    component: LoginPage,
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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
