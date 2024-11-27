<template>
    <div class="request">
      <div class="text">
        <div>혹시 원하는 주류가 검색이 안되시나요?</div>
        <div>저희에게 알려주시면 빠르게 추가해드리겠습니다</div>
        <div>저희 술고래를 이용해주셔서 감사합니다 :)</div>
      </div>
    <div class="q-gutter-y-md column">
      <q-input v-model="state.text" filled clearable clear-icon="close" type="textarea">
        </q-input>

      <q-btn class="btn" @click="sendRequest(state.text)" label="전송">
      </q-btn>
    </div>
    </div>
</template>

<style scoped>

div{font-family: 'MaruBuri';
font-size:20px;
}

.btn{
  background-color:#8faadc;
}
.text{
  margin-bottom: 50px;
  flex-direction: column;
  display:flex;
  justify-content: center;
  align-items: center;
}
.request{
  flex-direction: column;
  display:flex;
  justify-content: center;
  align-items: center;
  margin-top:100px;
}

.q-gutter-y-md{
  min-width: 400px;
  max-width:1000px;
}
</style>

<script>
import store from '@/store'
import { reactive } from 'vue'

export default {
  name: 'RequestPage',
  setup () {
    const state = reactive({
      text: '',
      isInputed: true
    })
    const settingDate=()=>{
      const now = new Date();
      const year = now.getFullYear();
      const month = ('0' + (now.getMonth() + 1)).slice(-2);
      const day = ('0' + now.getDate()).slice(-2);
      const dateString = year + '-' + month  + '-' + day;
      const hours = ('0' + now.getHours()).slice(-2); 
      const minutes = ('0' + now.getMinutes()).slice(-2);
      const seconds = ('0' + now.getSeconds()).slice(-2); 
      const timeString = hours + ':' + minutes  + ':' + seconds;
      return dateString+' '+timeString;
    }
    const sendRequest = (input) => {
      if (!input) {
        state.isInputed = false
        return
      }
      state.isInputed = true
      const date=settingDate()
      const msg={
        Text:input,
        Date:date,
        reqeust_token:false,
      }
      store.dispatch("sendRequest",msg);
    }
    return {
      state,
      sendRequest
    }
  }
}
</script>
