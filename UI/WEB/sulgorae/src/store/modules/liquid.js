
import axios from 'axios'
import index from '@/api/index'

export const liquid = {
    state:{
        LiquorDB:localStorage.getItem('LiquorDB')||'',
        InventoryDB:localStorage.getItem('InventoryDB')||'',       
    },
    // mutations:{
    //     inventory(){
    //         console.log("request_inventoryDB");
    //         const Kiosk_ID=localStorage.getItem('Kiosk_ID')
    //         axios({
    //             url:index.main.inventory(Kiosk_ID),
    //             methods:'get',
    //             data:Kiosk_ID
    //         })
    //         .then(res=>{
    //             console.log("재고 DB 목록들");
    //             console.log(res.data);
    //             localStorage.setItem('Inventory');
    //             console.log("inventory 함수안")
    //             return res;
    //         })
    //         .catch(()=>{
    //             console.log("재고가 없습니다");
    //             return "error";
    //         })    
    //     },

    // },
    actions:{
        saveLiquor(Liquor){
            localStorage.setItem('search_Liquor',Liquor);
        },
        // searchForAdd({dispatch}, Liquor_Name){
        //  // console.log("serchForAdd");
        //     // console.log(Liquor_Name)
        //     const Kiosk_ID=localStorage.getItem('Kiosk_ID')
        //     axios({
        //         url:index.main.searchForAdd(Kiosk_ID,Liquor_Name),
        //         method:'get',
        //         timeout: 2000,
        //     })
        //     .then(res=>{
        //         // console.log("목록들");
        //         // console.log(res.data);
        //         localStorage.removeItem('search_Liquor');
        //         dispatch('saveLiquor',res.data);
        //     })
        //     .catch(()=>{
        //         // console.log("검색된 주류가 없습니다");
        //         alert("검색된 주류가 없습니다")
        //     })
        // },
        addLiquor(state,Liquor){
            // console.log("addLiquor");
            // console.log(Liquor);
            const Kiosk_ID=localStorage.getItem('Kiosk_ID')
            axios({
                url:index.main.addLiquid(Kiosk_ID,Liquor.Liq_ID),
                method:'post',
                data:Liquor,
                timeout: 2000,
            })
            .then(()=>{
                // console.log(res.data);
                // console.log("추가되었습니다");
                alert("추가되었습니다")
            })
            .catch(()=>{
                // console.log("이미 추가된 주류 입니다");
                alert("이미 추가된 주류입니다")
            })
        },
        editLiquor(state, Liquor){
            // console.log("EditLiquor");
            // console.log(Liquor);
            const Kiosk_ID=localStorage.getItem('Kiosk_ID')
            axios({
                url:index.main.editLiquid(Kiosk_ID),
                method:'post',
                data:Liquor,
                timeout: 2000,
            })
            .then(()=>{
                // console.log(res.data);
                // console.log("수정 되었습니다");
                alert("수정되었습니다")
            })
            .catch(()=>{
                // console.log("수정에 실패하였습니다");
                alert("수정에 실패하였습니다")
            })
        },
        sendRequest(state,msg){
            // console.log("sendReqest");
            // console.log(msg);
            axios({
                url:index.main.request(),
                method:'post',
                data:msg,
                timeout: 2000,
            })
            .then(()=>{
                // console.log("메세지가 전달되었습니다");
                alert("메세지가 전달되었습니다")
            })
            .catch(()=>{
                // console.log("메세지 전송에 실패하였습니다");
                alert("메세지 전송에 실패하였습니다")
            })

        }
    }
}