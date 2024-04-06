import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createAuth0 } from '@auth0/auth0-vue';

const app = createApp(App);

app.use(router)

app.use(
  createAuth0({
    domain: "dev-wgq5om23cjf6zw6b.us.auth0.com",
    clientId: "vgCflcSrEPdBQ1K2pm6avIVgYTfJo5pW",
    authorizationParams: {
      redirect_uri: window.location.origin
    }
  })
);

app.mount('#app');