<template>
    <v-footer dark padless app inset>
        <v-card class="flex" flat tile color="orange" :elevation="10">
            <v-card-text class="py-2 white--text text-center">

                <v-layout column align-center>
                    <v-img class="mx-2" max-height="120" src="ahm_branding.png" max-width="120"></v-img>
                </v-layout>
              {{new Date().getFullYear()}}
            </v-card-text>
        </v-card>
    </v-footer>

</template>

<script>
    export default {
        name: "Footer"
    }
</script>

<style scoped>

</style>
