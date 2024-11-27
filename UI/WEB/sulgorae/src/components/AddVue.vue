<template>
  <q-card class="column" style="min-width: 800px; min-height:80%">

    <q-card-section  flex-direction:row>
      <q-input square filled v-model="state.text" :dense="state.dense">
        <template v-slot:prepend>
          <q-icon v-if="state.text === ''" name="search" />
          <q-icon v-else name="clear" class="cursor-pointer" @click="state.text = ''" />
        </template>
        <template v-slot:append>
          <q-btn round dense flat label="검색" @click="searchForAdd(state.text)"/>
        </template>
      </q-input>
    </q-card-section>

  <div class="q-pa-md">
    <q-table
      title="주류 목록"
      :rows="search_Inventory"
      :columns="columns"
      row-key="Name"
      table-colspan="12"
      v-if="search_click"
    >
<!-- :rows="search_Inventory" -->
      <template v-slot:header="props">
        <q-tr :props="props">
          <q-th auto-width />
          <q-th
            v-for="col in props.cols"
            :key="col.name"
            :props="props"
          >
            {{ col.label }}
          </q-th>
        </q-tr>
      </template>

      <template v-slot:body="props">
        <q-tr :props="props">
          <q-td auto-width>
            <q-btn v-if="!props.expand" size="sm" class="addBtn" round dense @click="addLiquor(props)" :icon="props.expand ? 'remove' : 'add'"/>
          
            <!-- <q-btn size="sm" color="accent" round dense @click="props.expand = !props.expand" :icon="props.expand ? 'remove' : 'add'" /> -->
          </q-td>
          <q-td
            v-for="col in props.cols"
            :key="col.name"
            :props="props"
          >
            {{ col.value }}
          </q-td>
        </q-tr>
      </template>

    </q-table>
  </div>
    
    <q-card-actions align="right" class="text-primary" style="" align-items="flex-end" >
      <q-btn class="closeBtn" flat color="deep-orange" label="닫기" v-close-popup />
    </q-card-actions>

  </q-card>
</template>

<style scoped>

.addBtn{
  background-color:#8faadc;
}

@font-face {
    font-family: 'MaruBuri';
    font-weight: 400; 
    font-style: normal; 
    src: url(https://cdn.jsdelivr.net/gh/webfontworld/naver/MaruBuri-Regular.woff2) format('woff2');
    font-display: swap;
  }
</style>

<script>
//import { stat } from 'fs'
import store from '@/store'
import { reactive } from 'vue'
import axios from 'axios'
import index from '@/api/index'
// import { mapActions } from 'vuex'

const columns = [
  {
    name: 'Name',
    required: true,
    label: '주류이름',
    align: 'left',
    field: row => row.Name,
    format: val => `${val}`,
    sortable: true
  },
  { name: 'Category', align: 'center', label: '주류종류', field: 'Category', sortable: true },
  { name: 'Capacity', label: '용량 (ml)', field: 'Capacity', sortable: true },
  { name : 'Country', label : '제조국',field:'Country'},
  { name: 'Alcohol', label: '도수 (%)', field: 'Alcohol' },
 ]

 const rows = [
]


export default {
  props:['Liquor_Inventory'],
  data(){
    return{
       search_click:false, //검색을 클릭했을 때 테이블이 보이도록 하기 위한 flag
       search_Inventory:[],
    }
  },
  methods:{
    //검색 버튼을 클릭했을 때 서버에 검색 요청을 보내는
    searchForAdd(Liq_name){
      this.search_click=true;
      // console.log(Liq_name)
      const Kiosk_ID=localStorage.getItem('Kiosk_ID')
      axios({
        url:index.main.searchForAdd(Kiosk_ID,Liq_name),
        method:'get',
        timeout: 2000,
      })
      .then(res=>{
        this.search_Inventory=res.data;
        // localStorage.removeItem('search_Liquor');
        // dispatch('saveLiquor',res.data);
      })
      .catch(()=>{
      // console.log("검색된 주류가 없습니다");
      alert("검색된 주류가 없습니다")
      })
    },
    addLiquor(props){
      props.expand=!props.expand;
      const check=this.Liquor_Inventory.find(v=>v.Liq_ID===props.row.Liq_ID);

      // console.log(check);

      if(check!=null){
        console.log("이미있음");
        alert("이미 추가한 주류 입니다");
        return
      }

      const Kiosk_ID=localStorage.getItem('Kiosk_ID')
      const Liq_data={
        Liq_ID:props.row.Liq_ID,
        Liq_Name:props.row.Name,
        Price:0,
        Amount:0,
        Recommend:0,
        Count:0,
        Kiosk_ID:Kiosk_ID,
        add_token:false,
      }
      store.dispatch("addLiquor",Liq_data);
    }
  },
  setup() {
    // const store=useStore()
    const state = reactive({
      text: '',
      dense: false,
      add:true,//true 일때 추가할 수 있다
    })
    //추가버튼 클릭시 재고 DB에 추가요청 보내기

return {
  state,
  columns,
  rows
  // ...mapActions(['searchForAdd'])
  // addSearch
}
  },
}
</script>
