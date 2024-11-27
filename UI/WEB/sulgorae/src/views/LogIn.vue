<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md column" style="max-width: 300px">
      <q-input v-model="state.Member_ID" label="ID" dense />
      <q-input v-model="state.Password" label="PW" dense type="password" />
      <div dense class="row justify-between">
        <q-btn flat color="primary" label="ID/PW 찾기" />
        <q-btn color="secondary" label="회원가입" router-link to="/signin" />
        <q-btn color="primary" label="로그인" @click="login(state)" />
      </div>
    </div>
  </div>
</template>

<style>
</style>

<script>
import router from '@/router'
import { reactive, computed } from 'vue'
import { useStore, mapActions } from 'vuex'

export default {
  name: 'LogIn',
  setup () {
    const state = reactive({
      Member_ID: '',
      Password: '',
    })

    const store = useStore()
    const isLoggedIn = computed(() => store.getters.isLoggedIn)

    if (isLoggedIn.value) {
      router.push({ name: 'main' })
    }

    return {
      state,
      ...mapActions(['login']),
    }
  },
}
</script>
