<template>
    <!--  <div>-->
    <v-container>
        <div class="text-center">
            <v-progress-circular v-if="loading && !healthStatusError"
                                 :size="100"
                                 color="primary"
                                 indeterminate
            >Fetching Status
            </v-progress-circular>
        </div>
        <v-layout row wrap>
            <template>
                <v-flex xs12 v-show="healthStatusError">
                    <v-alert border="top" type="error" class="title text-center">HealthCheck API appears to be offline,
                        Check back later !!
                    </v-alert>
                </v-flex>
            </template>
            <v-flex xs12 sm6 md4 v-for="service in services" :key="service.name">
                <v-card :color="service.status ? 'green' : 'red'" dark class="text-center ma-3">
                    <v-card-title class="headline font-weight-bold">{{service.name}}</v-card-title>
                    <v-divider></v-divider>
                    <v-card-actions>
                        Last checked {{lastDateTime}}
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>

    <!--  </div>-->
</template>

<script>
    import axios from 'axios'
    import moment from 'moment'

    export default {
        name: 'Dashboard',

        data: () => ({
            loading: true,
            services: '',
            lastDateTime: '',
            healthStatusError: false

        }),
        created() {
            this.getHealthStatus();
            this.timer = setInterval(this.getHealthStatus, 300000)
        },
        beforeDestroy() {
            clearInterval(this.timer)
        },
        methods: {
            getHealthStatus() {
                this.healthStatusError = false //remove error banner
                this.lastDateTime = moment().format('LTS')
                axios
                    .get(process.env.VUE_APP_BACKEND_BASE_URL + process.env.VUE_APP_BACKEND_HEALTHCHECK_ENDPOINT)
                    .then(response => {
                        this.services = response.data
                        this.loading = false
                    })
                    .catch(error => {
                        console.log(error)
                        this.healthStatusError = true
                    })

            },
            sleep(ms) {
                return new Promise(
                    resolve => setTimeout(resolve, ms)
                );
            }
        }

    };
</script>
