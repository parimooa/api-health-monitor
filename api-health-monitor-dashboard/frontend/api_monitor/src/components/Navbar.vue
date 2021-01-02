<template>
    <nav>
        <v-app-bar color="orange" dark app>
            <v-app-bar-nav-icon @click.stop="drawer=!drawer">
            </v-app-bar-nav-icon>
            <v-img class="mx-2" src="ahm_branding.png" max-height="100"
                   max-width="100" contain></v-img>
            <v-toolbar-title class="ml-2 font-weight-bold">
                API Health Monitor
            </v-toolbar-title>
        </v-app-bar>
        <v-navigation-drawer v-model="drawer" dark app class="red darken-4">
            <v-layout column align-center>
                <v-img src="ahm_branding.png"></v-img>
            </v-layout>
            <v-list flat>
                <v-list-item v-for="link in links" :key="link.text" router :to="link.route" active-class="border">
                    <v-list-item-action>
                        <v-icon>{{link.icon}}</v-icon>
                    </v-list-item-action>
                    <v-list-item-content>
                        <v-list-item-title>{{link.text}}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </nav>
</template>

<script>
    export default {
        name: "Navbar",
        data: () => ({
            drawer: true,
            links: [
                {icon: 'dashboard', text: 'Dashboard', route: '/'},
                // {icon:'folder',text:'Projects', route:'/projects'},
                // {icon:'person',text:'Team', route:'/team'},
            ]
        })
    }
</script>

<style scoped>
    .border {
        border-left: 4px solid
    }
</style>