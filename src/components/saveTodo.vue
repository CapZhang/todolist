<template>
    <section>
        <div class="todo-save">
            <button v-on:click="saveItem">保存</button>
        </div>
    </section>
</template>

<script>
export default {
    methods: {
        saveItem() {
            console.log(this.$store.state.items);
            this.$https
            .post("/todo/post",this.$store.state.items)
            .then(
                res=>{
                    console.log("res=>",res);
                }
            )
        }
    },
}
</script>