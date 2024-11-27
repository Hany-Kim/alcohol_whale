<template>
  <!-- relative로 수정하는 게 좋을 듯? -->
  <q-card style="min-width: 400px" >

  <q-card-section class="row justify-between">
    <span class="text-h6">주류 정보 수정</span>
    <q-btn flat>
      <q-icon v-if="changedInfo.Recommend" name="star" @click="changedInfo.Recommend = 0"/>
      <q-icon v-else name="star_outline" @click="changedInfo.Recommend = 1"/>
    </q-btn>
  </q-card-section>

  <q-card-section class="q-pt-none">
    <q-input borderless v-model="changedInfo.Liq_Name" label="이름" disable />
    <q-input v-model="changedInfo.Price" label="가격" />
    <q-input v-model="changedInfo.Amount" label="수량" />
    <q-input borderless v-model="changedInfo.Count" label="추천횟수" disable />
  </q-card-section>

  <q-card-actions align="right" class="text-primary">
    <q-btn flat label="저장" @click="sendInfo(changedInfo)" v-close-popup color="daef3"/>
    <q-btn flat color="deep-orange" label="닫기" v-close-popup />
  </q-card-actions>

  </q-card>
</template>
<style scoped>
@font-face {
    font-family: 'MaruBuri';
    font-weight: 400; 
    font-style: normal; 
    src: url(https://cdn.jsdelivr.net/gh/webfontworld/naver/MaruBuri-Regular.woff2) format('woff2');
    font-display: swap;
  }
</style>

<script>
import store from '@/store'
  export default {
    props: {
      information: {
        type: Object,
        required: true,
      },
    },
    data() {
      return  {
        changedInfo: this.information
      }
    },
    setup () {
      const sendInfo = (Liquor) => {
        // console.log(Liquor)
        //서버로 요청보내기
        const Liq_data={
          Kiosk_ID:Liquor.Kiosk_ID,
          Liq_ID:Liquor.Liq_ID,
          Price:Liquor.Price,
          Amount:Liquor.Amount,
          Recommend:Liquor.Recommend,
          edit_token:false,
        }
        store.dispatch("editLiquor",Liq_data);
      }
      return {
        sendInfo,
      }
    }
  }
</script>
