<template>
    <div class="centered-container">
      <div class="content">
        <h1>Automatic AI Evaluation for Student Assignments</h1>
        <p>This application revolutionizes the way assignments are evaluated by leveraging the power of Artificial Intelligence. It automatically assesses student submissions, providing instant, accurate feedback and grades. Designed to support educators in managing their workload more efficiently, our tool ensures a fair and consistent evaluation process, enabling students to learn and improve their skills effectively.</p>
        <button @click="goToDemo" class="demo-button">View Demo</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AiEvaluationInfo',
    methods: {
      goToDemo() {
        this.$router.push('/form') 
        // window.location.href = 'https://example.com/demo' for external URL redirection
      },
    },
  };
  </script>
  
  <style scoped>
  .centered-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 90vh; /* Reduced height to create space from the top */

    text-align: center;
    padding: 20px;
  }
  
  .content {
    width: 40%; /* Set the width to occupy the middle 40% */
    max-width: 600px; /* Optional: You can adjust or remove this to control the maximum width */
  }
  
  h1 {
    font-size: 24px;
    margin-bottom: 20px;
  }
  
  p {
    font-size: 16px;
    line-height: 1.6;
  }
  
  .demo-button {
    margin-top: 20px;
    padding: 10px 20px;
    font-size: 16px;
    color: white;
    background-color: #007bff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .demo-button:hover {
    background-color: #0056b3;
  }
  </style>
  