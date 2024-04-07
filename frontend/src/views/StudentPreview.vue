<template>
    <div class="assignment-preview">
      <div class="assignment-header">
        <div>
          <h2>UX/UI: Prototype design</h2>
          <p class="grade">Grade: <span>8/10</span></p>
        </div>
        <div class="grade-badge">8/10</div>
      </div>
      <div class="assignment-body">
        <div class="assignment-note">
          <p><strong>Note:</strong> Your prototype showcases a good level of creativity, and your approach to solving the design problem is commendable. However, there was room for more innovative features that could have set your design apart from existing solutions.</p>
          <button class="download-btn">Download full note</button>
        </div>
        <div class="assignment-details">
          <p><strong>Submitted file:</strong> Valovska.pdf</p>
          <div class="file-preview">
            <!-- Image preview or icon here -->
          </div>
        </div>
      </div>
      <div class="assignment-footer">
        <p>Submission attempts: 12</p>
        <p>Submission time: 6.4.2024 11:59</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AssignmentPreview',
    // other component options
  };
  </script>
  
  <style scoped>
  .assignment-preview {
    font-family: Arial, sans-serif;
    max-width: 700px;
    margin: auto;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-top: 5%;
  }
  
  .assignment-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .assignment-header h2 {
    margin: 0;
    color: #2c3e50;
  }
  
  .grade {
    font-size: 18px;
    color: #27ae60;
  }
  
  .grade-badge {
    background-color: #27ae60;
    color: white;
    padding: 10px;
    border-radius: 5px;
    font-size: 18px;
  }
  
  .assignment-body {
    border-top: 1px solid #ddd;
    border-bottom: 1px solid #ddd;
    padding: 20px 0;
  }
  
  .assignment-note strong {
    color: #2c3e50;
  }
  
  .download-btn {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 10px;
  }
  
  .download-btn:hover {
    background-color: #229954;
  }
  
  .assignment-details {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 20px;
  }
  
  .file-preview {
    /* Add styles for file preview if necessary */
  }
  
  .assignment-footer {
    display: flex;
    justify-content: space-between;
    padding-top: 20px;
  }
  
  .assignment-footer p {
    margin: 0;
    color: #7f8c8d;
  }
  </style>
  