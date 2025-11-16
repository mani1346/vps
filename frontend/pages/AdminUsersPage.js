export default {
    name: "AdminUsersPage",
    template: `
        <div class="container mt-4">
            <h2 class="mb-4">Users</h2>
            <div v-if="loading" class="text-center">Loading users...</div>
            <div v-if="error" class="alert alert-danger">{{ error }}</div>
            <div class="card shadow-sm" v-if="!loading && !error">
                <div class="card-body">
                    <table class="table">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Vehicle Number</th>
                                </tr>
                        </thead>
                        <tbody>
                            <tr v-for="user in users" :key="user.id">
                                <td>{{ user.id }}</td>
                                <td>{{ user.first_name }} {{ user.last_name }}</td>
                                <td>{{ user.email }}</td>
                                <td>{{ user.vehicle_number }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    `,
    data() {
        return {
            users: [],
            loading: true,
            error: null,
        };
    },
    methods: {
        async fetchUsers() {
            this.loading = true;
            this.error = null;
            try {
                const res = await fetch('/api/admin/users', {
                    headers: {
                        'Authentication-Token': this.$store.state.auth_token,
                    },
                });
                if (!res.ok) {
                    throw new Error('Could not fetch users.');
                }
                this.users = await res.json();
            } catch (e) {
                this.error = e.message;
            } finally {
                this.loading = false;
            }
        }
    },
    async mounted() {
        await this.fetchUsers();
    },
}