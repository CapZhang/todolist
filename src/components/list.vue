<template>
<section>
   <ul class="todo-list" v-show="list.length">
     <li class="todo-item" v-for="(item,index) in list" v-bind:key="index+item">
       <span>{{index+1}}.</span><p>{{item}}</p><button @click="removeItem(index)">完成</button>
     </li>
   </ul>
   <div class="todo-nodata" v-show="!list.length">
     恭喜你完成所有内容，请继续添加！！
   </div>
 </section>
</template>

<script>
import Bus from "../Bus"
export default {
    // props:{
    //     childrenList:{ type:Array }
    // },
    
  data() {
    return {
      list:["吃饭","睡觉","撸猫"],
    }
  },
  beforeMount(){
    Bus.$on('addItem',text=>{
      this.list.push(text)
    })
  },
    methods:{
        removeItem(index){
            // this.$emit("removeItem",index)
            this.list.splice(index)
        }
    }
    
}
</script>