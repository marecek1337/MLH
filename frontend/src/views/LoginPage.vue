<template>
  <div>
    <nav class="navbar">
      <div class="container">
        <span class="brand">Ring</span>
        <div class="nav-items">
          <button v-if="!isAuthenticated" @click="login" class="nav-button">Log In</button>
          <div v-if="isAuthenticated" class="user-info">
            <span class="user-name">{{ user.name }}</span>
            <button @click="logout" class="nav-button logout">Log Out</button>
          </div>
        </div>
      </div>
    </nav>
    <div class="profile-container" v-if="isAuthenticated">
      <h2>Signed user</h2>
      <p><strong>Name:</strong> {{ user.name }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
    </div>
  </div>
</template>

<script>
import { useAuth0 } from '@auth0/auth0-vue';

export default {
  setup() {
    const { loginWithRedirect, logout, user, isAuthenticated } = useAuth0();

    return {
      login: () => {
        loginWithRedirect();
      },
      logout: () => {
        logout({ returnTo: window.location.origin });
      },
      user,
      isAuthenticated
    };
  }
};
</script>

<style scoped>
.navbar {
  background-color: #f5f5f5;
  padding: 10px 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.container {
  width: 90%;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.brand {
  font-weight: bold;
  font-size: 24px;
}

.nav-items {
  display: flex;
  align-items: center;
}

.user-info {
  display: flex;
  align-items: center;
}

.user-name {
  margin-right: 20px;
  font-weight: bold;
}

.nav-button, .logout {
  cursor: pointer;
  border: none;
  outline: none;
  background-color: #007bff;
  color: white;
  padding: 8px 16px;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.logout {
  background-color: #dc3545;
}

.nav-button:hover, .logout:hover {
  background-color: #0056b3;
}

.profile-container {
  width: 90%;
  margin: 20px auto;
}

h2 {
  color: #333;
}

p {
  color: #666;
}
</style>
