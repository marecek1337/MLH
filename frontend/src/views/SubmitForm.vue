<template>
    <div class="evaluation-form">
      <h2>Evaluation of Assignment</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="assignment-name">Assignment Name</label>
          <input type="text" id="assignment-name" v-model="form.assignmentName"  />
        </div>
  
        <div class="form-group">
          <label for="subject">Subject</label>
          <select id="subject" v-model="form.subject" >
            <option value="UX">UX/UI</option>
            <option value="Engineering">Engineering</option>
            <option value="Software Architecture">Software Architecture</option>
          </select>
        </div>
  
        <div class="form-group">
          <label for="max-score">Max Score</label>
          <input type="number" id="max-score" v-model="form.maxScore"  />
        </div>
  
        <div class="form-group">
          <label for="description">Description</label>
          <textarea id="description" v-model="form.description" placeholder="Enter prompt for evaluation criteria" ></textarea>
        </div>
  
        <div class="form-group">
          <label for="format">Format</label>
          <select id="format" v-model="form.format" >
            <option value="pdf">PDF</option>
            <option value="jpg">JPG</option>
            <option value="docx">DOCX</option>
            <option value="txt">TXT</option>
          </select>
        </div>
  
        <button type="submit">Submit Evaluation</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'EvaluationForm',
    data() {
      return {
        form: {
          assignmentName: '',
          subject: '',
          maxScore: null,
          description: '',
          format: ''
        }
      };
    },
    methods: {
      submitForm() {
        console.log(JSON.stringify(this.form, null, 2));
        // Here you would typically send this data to a server
        this.$router.push('listOfStudents') 
      }
    }
  };
  </script>
  
  <style scoped>
  .evaluation-form {
    max-width: 500px;
    margin: 0 auto;
    padding: 2em;
    background: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .evaluation-form h2 {
    color: #333;
    text-align: center;
  }
  
  .form-group {
    margin-bottom: 1em;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 0.5em;
  }
  
  .form-group input[type="number"],
  .form-group textarea,
  .form-group select {
    width: 100%;
    padding: 0.75em;
    border-radius: 4px;
    border: 1px solid #ccc;
  }
  
  .form-group textarea {
    resize: vertical;
  }
  
  button[type="submit"] {
    width: 100%;
    padding: 1em;
    border: none;
    background-color: #04AA6D;
    color: white;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1em;
  }
  
  button[type="submit"]:hover {
    background-color: #037d56;
  }
  </style>
  