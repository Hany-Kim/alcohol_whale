<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md column" style="max-width: 300px">
      <q-input v-model="state.Member_ID" label="ID" >
        <template v-slot:append>
          <q-btn dense color="primary" @click="duplicateCheck(state.Member_ID)" :disabled="!state.Member_ID">중복 확인</q-btn>
        </template>
      </q-input>
      <q-input v-model="state.Password" label="PW" type="password" />
      <q-input v-model="state.PasswordConfirm" label="PW Confirm" type="password" />
      <q-input v-model="state.Name" label="이름" />
      <q-input v-model="state.Kiosk_ID" label="키오스크 번호"  />
      <q-input v-model="state.Phone" label="휴대폰" placeholder="010-1234-5678" />
      <q-input v-model="state.Email" label="이메일" />
      <q-btn color="primary" label="회원 가입" @click="signin(state)"/>
      <q-btn flat color="deep-orange" label="취소" router-link to="/login" />
    </div>
  </div>
</template>

<style>
</style>

<script>
import { reactive } from 'vue'
import { mapActions } from 'vuex'
import index from '@/api/index'
import axios from 'axios'

export default {
  name: 'SignIn',
  setup () {
    const state = reactive({
      Member_ID: '',
      Member_IDConfirm: '',
      Password: '',
      PasswordConfirm: '',
      Name: '',
      Kiosk_ID: '',
      Phone: '',
      Email: '',
    })

    // ID 중복 확인 후 기록 위해 axios 사용
    // 이것도 store/modules/account.js에서 처리하도록 수정하면 좋을 거 같음
    const duplicateCheck = (target) => {
      const body={
        Member_ID:target
        };
      console.log(body);
      axios({
        url: index.account.idconfirm(target),
        method: 'get',
        timeout: 2000,
        data:target,
      }).then(() => {
        state.Member_IDConfirm = state.Member_ID
        alert("사용 가능한 아이디입니다!")
      }).catch((err) => {
        console.log(err);
        alert("이미 존재하거나, 사용할 수 없는 아이디입니다.")
      })
    }

    return {
      state,
      duplicateCheck,
      ...mapActions(['signin'])
    }
  },
}
</script>
