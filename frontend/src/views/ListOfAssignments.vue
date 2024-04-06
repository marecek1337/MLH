<template>
    <div class="grades-table">
        <table>
            <thead>
                <tr>
                    <th>Assignment</th>
                    <th>Subject</th>
                    <th>Grade</th>
                    <th>Detail</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in assignments" :key="item.id" @click="goToDetail(item.detailUrl)"
                    :class="{ 'no-grade': !item.grade }">
                    <td>{{ item.assignment }}</td>
                    <td>{{ item.subject }}</td>
                    <td>{{ item.grade !== null ? item.grade : '---' }}</td>
                    <td><button>Detail</button></td>
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
            assignments: [
                {
                    "id": 1,
                    "assignment": "Wireframe Demo",
                    "subject": "UX/UI",
                    "grade": null,
                    "detailUrl": "#"
                },
                {
                    "id": 2,
                    "assignment": "Prototype design",
                    "subject": "UX/UI",
                    "grade": 8,
                    "detailUrl": "#"
                },
                {
                    "id": 3,
                    "assignment": "Entity–relationship model",
                    "subject": "Database systems",
                    "grade": 8,
                    "detailUrl": "#"
                },
                {
                    "id": 4,
                    "assignment": "Entity–relationship model",
                    "subject": "Database systems",
                    "grade": 4,
                    "detailUrl": "#"
                },
                {
                    "id": 5,
                    "assignment": "User Persona Creation",
                    "subject": "UX/UI",
                    "grade": 9,
                    "detailUrl": "#"
                },
                {
                    "id": 6,
                    "assignment": "Playtesting",
                    "subject": "UX/UI",
                    "grade": 2,
                    "detailUrl": "#"
                }
            ]
        };
    },
    methods: {
        goToDetail(url) {
            window.location.href = url;
        }
    }
};
</script>

<style scoped>
.grades-table table {
    width: 100%;
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
    padding-top: 12px;
    padding-bottom: 12px;
    background-color: #04AA6D;
    color: white;
}

.grades-table .no-grade {
    background-color: #ffdddd;
}

.grades-table button {
    cursor: pointer;
}
</style>