<template>
  <div class="q-pa-md">
    <q-table
      @row-click="openEdit"
      :rows="Liquor_Inventory"
      :columns="$q.screen.gt.xs ? $q.screen.gt.sm ? columns : columnsMid : columnsMinimum"
      row-key="name"
      :rows-per-page-options="[10, 20]"
      no-data-label="재고 주류가 없습니다"
    >

      <template v-slot:bottom-row >
        <q-tr @click="openAdd">
          <q-td colspan="100%" class="text-center">
            <q-icon name="add_circle_outline" style="color:#8faadc; font-size:2rem;" />
          </q-td>
        </q-tr>
      </template>
    </q-table>
  </div>
  <div>
  <q-dialog v-model="state.prompt" persistent>
    <EditVue :information="state.selected" />
  </q-dialog>
  </div>
  <div>
    <q-dialog v-model="state.addView" persistent>
      <AddVue v-bind:Liquor_Inventory="Liquor_Inventory"/>
    </q-dialog>
  </div>
</template>
<style scoped>


</style>
<script>
import { reactive } from 'vue'
import EditVue from '../components/EditVue.vue'
import AddVue from '../components/AddVue.vue'
import axios from 'axios'
import index from '@/api/index'

const columns = [
  { name: 'Liq_Name', label: '이름', align: 'left', field: row => row.Liq_Name, sortable: true },
  { name: 'Price', label: '가격 (원)', field: 'Price', sortable: true },
  { name: 'Amount', label: '재고 (개)', field: 'Amount', sortable: true },
  { name: 'Count', label: '추천횟수', field: 'Count', sortable: true },
  { name: 'Recommend', label: '즐겨찾기', field: 'Recommend', sortable: true }
]

const columnsMid = [
  { name: 'Liq_Name', label: '이름', align: 'left', field: row => row.Liq_Name, sortable: true },
  { name: 'Price', label: '가격 (원)', field: 'Price', sortable: true },
  { name: 'Amount', label: '재고 (개)', field: 'Amount', sortable: true },
  { name: 'Count', label: '추천횟수', field: 'Count', sortable: true },
  { name: 'Recommend', label: '즐겨찾기', field: 'Recommend', sortable: true }
]

const columnsMinimum = [
  { name: 'Liq_Name', label: '이름', align: 'left', field: row => row.Liq_Name, sortable: true },
  { name: 'Price', label: '가격 (원)', field: 'Price', sortable: true },
  { name: 'Amount', label: '재고 (개)', field: 'Amount', sortable: true },
  { name: 'Count', label: '추천횟수', field: 'Count', sortable: true },
  { name: 'Recommend', label: '즐겨찾기', field: 'Recommend', sortable: true }
]

 const rows =[];
//       {
//         Inven_ID: 3,
//         Liq_ID: 1,
//         Liq_Name: '와일드터키 8',
//         Price: 79200,
//         Amount: 20,
//         Recommend: true,
//         Count: 4,
//         Kiosk_ID:'123456',
//       },
//       {
//         Inven_ID: 6,
//         Liq_ID:16,
//         Liq_Name: '처음처럼',
//         Price: 2000,
//         Amount: 300,
//         Recommend: false,
//         Count:1,
//         Kiosk_ID:'123456',
//       },
//     ]


// 주류 DB를 받고 해당 양식에 맞게 가공
// 아니면 여기 코드를 고쳐도 되고.

export default {
  name: 'MainPage',
  components: {
    EditVue,
    AddVue,
  },
  data(){
    return{
      seen:false,
      Liquor_Inventory:[]
      }
  },
  methods:{
    loading(){
        const Kiosk_ID=localStorage.getItem('Kiosk_ID')
        axios({
          url:index.main.inventory(Kiosk_ID),
          method:'get',
          data:Kiosk_ID,
          timeout: 2000,
        })
       .then(res=>{
          // console.log("재고 DB 목록들");
          // console.log(res.data);
          this.Liquor_Inventory=res.data;
          // console.log(this.Liquor_Inventory);
        })
        .catch(()=>{
          //console.log("재고가 없습니다");
        })
    }
  },
  setup () {
    const state = reactive({
      prompt: false,
      addView: false,
      selected: '',
    })
    const openEdit = (event, target) => {
      state.prompt = true
      state.selected = target
    }
    const openAdd = () => {
      state.addView = true
    }
    return {
      state,
      openEdit,
      openAdd,
      columns,
      columnsMid,
      columnsMinimum,
      rows,
    }
  },
  mounted(){
    this.loading();
  }
}
</script>
