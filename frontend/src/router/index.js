import { createWebHistory, createRouter } from "vue-router";
import LoginPage from "@/views/LoginPage.vue";
import assignemntPreview from "@/views/AssignmentPreview.vue";
import linkOfAssignments from "@/views/ListOfAssignments.vue";



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
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
