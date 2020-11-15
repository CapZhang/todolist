<template>
<section>
   <ul class="todo-list" v-show="childrenList.length">
     <li class="todo-item" v-for="(item,index) in childrenList" v-bind:key="index+item">
       <span>{{index+1}}.</span><p>{{item}}</p><button @click="removeItem(index)">完成</button>
     </li>
   </ul>
   <div class="todo-nodata" v-show="!childrenList.length">
     恭喜你完成所有内容，请继续添加！！
   </div>
 </section>
</template>

<script>
export default {
    props:{
        childrenList:{ type:Array }
    },
    methods:{
        removeItem(index){
            this.$emit("removeItem",index)
        }
    }
    
}
</script>