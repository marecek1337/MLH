<template>
  <div class="grades-table">
    <table>
      <thead>
        <tr>
          <th>Student Name</th>
          <th>Grade</th>
          <th>Details</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.id" @click="goToDetail(student.id)">
          <td>{{ student.name }}</td>
          <td>{{ student.grade }}</td>
          <td><button class="view-btn">View</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'GradesTable',
  data() {
    return {
      students: this.generateStudents(10),
    };
  },
  methods: {
    generateStudents(count) {
      return Array.from({ length: count }, (_, i) => ({
        id: i + 1,
        name: `Student ${i + 1}`,
        grade: Math.ceil(Math.random() * 10),
      }));
    },
    goToDetail(id) {
      window.location.href = `student/${id}`;
    },
  },
};
</script>

<style scoped>
.grades-table {
  display: flex;
  justify-content: center;
  margin: 20px 0;
}

.grades-table table {
  width: 60%;
  border-collapse: collapse;
}

.grades-table th,
.grades-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.grades-table tr:nth-child(even) {
  background-color: #f2f2f2;
}

.grades-table tr:hover {
  background-color: #ddd;
}

.grades-table th {
  background-color: #007bff;
  color: white;
}

.view-btn {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
}

.view-btn:hover {
  background-color: #0056b3;
}
</style>
