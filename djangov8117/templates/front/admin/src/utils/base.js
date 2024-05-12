const base = {
    get() {
        return {
            url : "http://localhost:8080/djangov8117/",
            name: "djangov8117",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/h5/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "摄影竞赛小程序"
        } 
    }
}
export default base
