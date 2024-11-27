<template>
  <div>
    <div class="select" >
      <button id="0" @click="requestTop5(0)">전체</button>
      <button id="1" @click="requestTop5(1)">위스키</button>
      <button id="2" @click="requestTop5(2)">리큐르</button>
      <button id="3" @click="requestTop5(3)">보드카</button>
    </div>
    <div v-if="nodata">데이터가 없습니다</div>
    <div class="chartBox">
      <canvas id="chart1" width="50%" height="50%"></canvas>
    </div>
  </div>
</template>
<style scoped>

@font-face {
    font-family: 'MaruBuri';
    font-weight: 400; 
    font-style: normal; 
    src: url(https://cdn.jsdelivr.net/gh/webfontworld/naver/MaruBuri-Regular.woff2) format('woff2');
    font-display: swap;
  }

.select{
  width:90%;
  /* position:absolute;
  left:50%;
  transform:translate(-50%,0%);  */
  margin: 30px;
  margin-left: auto; margin-right: auto;
}

button{
  width:25%;
  height:50px;
  background-color: white;
  border: 2px;
  font-family: 'MaruBuri';
  font-size:large;
}
.chartBox{
  width:50%;
   margin-left: auto; margin-right: auto;
}

</style>

<script>
import {Chart,registerables} from 'chart.js';
Chart.register(...registerables);
import axios from 'axios'
import index from '@/api/index'

export default{
  name:'app',
  data(){
    return{
      myChart:null,  //그래프
      Top5Inventory:[], //top5 데이터
      list_liquor:['whole','whisky','liqueur','vodka'],  //그래프 분류
      select:0,   //어떤 그래프 그릴지 선택변수
      chart_create:false,  //그래프가 그려져 있는지
      nodata:true
    }
  },
  methods:{
    setBackgroundcolor(category){
      const btn= document.getElementById(this.select);
      btn.style.backgroundColor="white";
      const id=document.getElementById(category);
      id.style.backgroundColor="#8faadc";
      this.select=category;
    },
    requestTop5(category){
      this.setBackgroundcolor(category);
      const Kiosk_ID=localStorage.getItem('Kiosk_ID')
        axios({
          url:index.main.graph(Kiosk_ID,this.list_liquor[category]),
          method:'get',
          timeout: 2000,
        })
       .then(res=>{
          console.log("TOP5 목록들");
          // console.log(res.data);
          this.Top5Inventory=res.data;
          this.fillData(this.Top5Inventory);
        })
        .catch(()=>{
          alert("TOP5를 가지고 오지 못했습니다");
          if(this.chart_create===true){
            this.myChart.destroy();
            this.chart_create=false;
          }
        })

    },
    //그래프 그리는 함수
    fillData(Top5Inventory){

      //그려진 그래프가 있으면 삭제
      if(this.chart_create===true){
        this.myChart.destroy();
      }

      //넘어온 데이터 갯수만큼 저장
      const labels=[];
      const data=[];
      const len=Top5Inventory.length;

      for(var i=0;i<len;i++){
        if(Top5Inventory[i].Count==0){
          break;
        }
        labels.push(Top5Inventory[i].Liq_Name);
        data.push(Top5Inventory[i].Count);
      }
      if(len==0 || data.length==0){
        this.nodata=true;
      }
      else{
        this.nodata=false;
      }

      //그래프 생성
      const ctx=document.getElementById("chart1");
      this.myChart=new Chart(ctx,{
        type:'doughnut',
        data:{
          labels:labels,
          datasets:[
            {
              backgroundColor:[
                 "#A684B7",
                "#78BAA1",
                "#DE9D11",
                "#E0D295",
                "#B1D166"
              ],
              data:data,
            }
          ]
        },
        options:{
          plugins:{
            legend:{
              display:true,
              position:"left",
              labels:{
                boxWidth:7,
                padding:10,
                usePointStyle:true,
                pointStyle:"circle",
                font:{
                  size:15
                }
              },
              fullSize:false,
              align:"center"
            },
            responsive:true,
            maintainAspectRatio:false,
            layout:{
              padding:{
                top:20,
                bottom:20
              }
            },
            elements:{
              arc:{
                borderWidth:0.2
              }
            },
            animation:{
              duration:1000
            }
          }
        }
      })
      this.chart_create=true;
    }

  },
  mounted(){
    this.requestTop5(0);
  }
};

</script>



