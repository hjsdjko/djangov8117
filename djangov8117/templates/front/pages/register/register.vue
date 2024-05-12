<template>
	<view class="content">
		<view class="logo" v-if="true">
			<image :style='{"boxShadow":"0 0 8rpx #D79468","borderColor":"#ccc","borderRadius":"20rpx","borderWidth":"0px","width":"160rpx","borderStyle":"solid","url":"http://codegen.caihongy.cn/20210901/22fe298c5b894c3d9d10eed9c8ca6a60.webp","isShow":true,"height":"160rpx"}' src='http://codegen.caihongy.cn/20210901/22fe298c5b894c3d9d10eed9c8ca6a60.webp' mode="aspectFill"></image>
		</view>
		<view v-if="tableName=='jiaoshi'" class="uni-form-item uni-column">
			<input :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}'  v-model="ruleForm.jiaoshigonghao" type="text" class="uni-input" name="" placeholder="教师工号" />
		</view>
		<view v-if="tableName=='jiaoshi'" class="uni-form-item uni-column">
			<input :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}'  v-model="ruleForm.mima" type="text" class="uni-input" name="" placeholder="密码" />
		</view>
		<view v-if="tableName=='jiaoshi'" class="uni-form-item uni-column">
			<input :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}'  v-model="ruleForm.jiaoshixingming" type="text" class="uni-input" name="" placeholder="教师姓名" />
		</view>
		<view v-if="tableName=='jiaoshi'" class="uni-form-item uni-column">
                        <picker  @change="jiaoshixingbieChange" :value="jiaoshixingbieIndex" :range="jiaoshixingbieOptions">
                                <view :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}' class="uni-input">{{ruleForm.xingbie?ruleForm.xingbie:"请选择性别"}}</view>
                        </picker>
                </view>
		<view v-if="tableName=='jiaoshi'" class="uni-form-item uni-column">
			<input :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}'  v-model="ruleForm.youxiang" type="text" class="uni-input" name="" placeholder="邮箱" />
		</view>
		<view v-if="tableName=='jiaoshi'" class="uni-form-item uni-column">
			<input :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}'  v-model="ruleForm.lianxishouji" type="text" class="uni-input" name="" placeholder="联系手机" />
		</view>
		<view v-if="tableName=='xuesheng'" class="uni-form-item uni-column">
			<input :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}'  v-model="ruleForm.xuehao" type="text" class="uni-input" name="" placeholder="学号" />
		</view>
		<view v-if="tableName=='xuesheng'" class="uni-form-item uni-column">
			<input :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}'  v-model="ruleForm.mima" type="text" class="uni-input" name="" placeholder="密码" />
		</view>
		<view v-if="tableName=='xuesheng'" class="uni-form-item uni-column">
			<input :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}'  v-model="ruleForm.xueshengxingming" type="text" class="uni-input" name="" placeholder="学生姓名" />
		</view>
		<view v-if="tableName=='xuesheng'" class="uni-form-item uni-column">
                        <picker  @change="xueshengxingbieChange" :value="xueshengxingbieIndex" :range="xueshengxingbieOptions">
                                <view :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}' class="uni-input">{{ruleForm.xingbie?ruleForm.xingbie:"请选择性别"}}</view>
                        </picker>
                </view>
		<view v-if="tableName=='xuesheng'" class="uni-form-item uni-column">
			<input :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}'  v-model="ruleForm.youxiang" type="text" class="uni-input" name="" placeholder="邮箱" />
		</view>
		<view v-if="tableName=='xuesheng'" class="uni-form-item uni-column">
			<input :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}'  v-model="ruleForm.shoujihaoma" type="text" class="uni-input" name="" placeholder="手机号码" />
		</view>
		<view v-if="tableName=='fudaoyuan'" class="uni-form-item uni-column">
			<input :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}'  v-model="ruleForm.gonghao" type="text" class="uni-input" name="" placeholder="工号" />
		</view>
		<view v-if="tableName=='fudaoyuan'" class="uni-form-item uni-column">
			<input :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}'  v-model="ruleForm.mima" type="text" class="uni-input" name="" placeholder="密码" />
		</view>
		<view v-if="tableName=='fudaoyuan'" class="uni-form-item uni-column">
			<input :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}'  v-model="ruleForm.xingming" type="text" class="uni-input" name="" placeholder="姓名" />
		</view>
		<view v-if="tableName=='fudaoyuan'" class="uni-form-item uni-column">
                        <picker  @change="fudaoyuanxingbieChange" :value="fudaoyuanxingbieIndex" :range="fudaoyuanxingbieOptions">
                                <view :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}' class="uni-input">{{ruleForm.xingbie?ruleForm.xingbie:"请选择性别"}}</view>
                        </picker>
                </view>
		<view v-if="tableName=='fudaoyuan'" class="uni-form-item uni-column">
			<input :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}'  v-model="ruleForm.youxiang" type="text" class="uni-input" name="" placeholder="邮箱" />
		</view>
		<view v-if="tableName=='fudaoyuan'" class="uni-form-item uni-column">
			<input :style='{"borderColor":"rgba(0, 0, 0, 0.6)","backgroundColor":"#fff","borderRadius":"8rpx","color":"rgba(51, 51, 51, 1)","textAlign":"left","borderWidth":"2rpx","fontSize":"26rpx","borderStyle":"solid","height":"60rpx"}'  v-model="ruleForm.shouji" type="text" class="uni-input" name="" placeholder="手机" />
		</view>
		<view>
			<button @tap="register" type="primary" :style='{"borderColor":"#ccc","backgroundColor":"rgba(215, 148, 104, 1)","borderRadius":"8rpx","color":"rgba(255, 255, 255, 1)","borderWidth":"0px","fontSize":"32rpx","borderStyle":"solid","height":"88rpx"}'>注册</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
                                jiaoshixingbieOptions: [],
                                jiaoshixingbieIndex: 0,
                                xueshengxingbieOptions: [],
                                xueshengxingbieIndex: 0,
                                fudaoyuanxingbieOptions: [],
                                fudaoyuanxingbieIndex: 0,
				ruleForm: {
				},
				emailcode: "",
				tableName:""
			}
		},
		async onLoad() {
			let res = [];
			let table = uni.getStorageSync("loginTable");
	    		this.tableName = table;

                        // 自定义下拉框值
			if(this.tableName=='jiaoshi'){
                this.jiaoshixingbieOptions = "男,女".split(',');
				this.ruleForm.xingbie=this.jiaoshixingbieOptions[0]
			}
                        // 自定义下拉框值
			if(this.tableName=='xuesheng'){
                this.xueshengxingbieOptions = "男,女".split(',');
				this.ruleForm.xingbie=this.xueshengxingbieOptions[0]
			}
                        // 自定义下拉框值
			if(this.tableName=='fudaoyuan'){
                this.fudaoyuanxingbieOptions = "男,女".split(',');
				this.ruleForm.xingbie=this.fudaoyuanxingbieOptions[0]
			}
			
			this.styleChange()
		},
		methods: {

                        // 下拉变化
                        jiaoshixingbieChange(e) {
                                this.jiaoshixingbieIndex = e.target.value
                                this.ruleForm.xingbie = this.jiaoshixingbieOptions[this.jiaoshixingbieIndex]
                        },
                        // 下拉变化
                        xueshengxingbieChange(e) {
                                this.xueshengxingbieIndex = e.target.value
                                this.ruleForm.xingbie = this.xueshengxingbieOptions[this.xueshengxingbieIndex]
                        },
                        // 下拉变化
                        fudaoyuanxingbieChange(e) {
                                this.fudaoyuanxingbieIndex = e.target.value
                                this.ruleForm.xingbie = this.fudaoyuanxingbieOptions[this.fudaoyuanxingbieIndex]
                        },

			styleChange() {
				this.$nextTick(()=>{
					// document.querySelectorAll('.uni-input .uni-input-input').forEach(el=>{
					//   el.style.backgroundColor = this.registerFrom.content.input.backgroundColor
					// })
				})
			},
			// 获取uuid
			getUUID () {
				return new Date().getTime();
			},
			// 注册
			async register() {
				if((!this.ruleForm.jiaoshigonghao) && `jiaoshi` == this.tableName){
					this.$utils.msg(`教师工号不能为空`);
					return
				}
				if((!this.ruleForm.mima) && `jiaoshi` == this.tableName){
					this.$utils.msg(`密码不能为空`);
					return
				}
				if((!this.ruleForm.jiaoshixingming) && `jiaoshi` == this.tableName){
					this.$utils.msg(`教师姓名不能为空`);
					return
				}
				if(`jiaoshi` == this.tableName && this.ruleForm.youxiang&&(!this.$validate.isEmail(this.ruleForm.youxiang))){
					this.$utils.msg(`邮箱应输入邮件格式`);
					return
				}
				if(`jiaoshi` == this.tableName && this.ruleForm.lianxishouji&&(!this.$validate.isMobile(this.ruleForm.lianxishouji))){
					this.$utils.msg(`联系手机应输入手机格式`);
					return
				}
				if((!this.ruleForm.xuehao) && `xuesheng` == this.tableName){
					this.$utils.msg(`学号不能为空`);
					return
				}
				if((!this.ruleForm.mima) && `xuesheng` == this.tableName){
					this.$utils.msg(`密码不能为空`);
					return
				}
				if((!this.ruleForm.xueshengxingming) && `xuesheng` == this.tableName){
					this.$utils.msg(`学生姓名不能为空`);
					return
				}
				if(`xuesheng` == this.tableName && this.ruleForm.youxiang&&(!this.$validate.isEmail(this.ruleForm.youxiang))){
					this.$utils.msg(`邮箱应输入邮件格式`);
					return
				}
				if(`xuesheng` == this.tableName && this.ruleForm.shoujihaoma&&(!this.$validate.isMobile(this.ruleForm.shoujihaoma))){
					this.$utils.msg(`手机号码应输入手机格式`);
					return
				}
				if((!this.ruleForm.gonghao) && `fudaoyuan` == this.tableName){
					this.$utils.msg(`工号不能为空`);
					return
				}
				if((!this.ruleForm.mima) && `fudaoyuan` == this.tableName){
					this.$utils.msg(`密码不能为空`);
					return
				}
				if((!this.ruleForm.xingming) && `fudaoyuan` == this.tableName){
					this.$utils.msg(`姓名不能为空`);
					return
				}
				if(`fudaoyuan` == this.tableName && this.ruleForm.youxiang&&(!this.$validate.isEmail(this.ruleForm.youxiang))){
					this.$utils.msg(`邮箱应输入邮件格式`);
					return
				}
				if(`fudaoyuan` == this.tableName && this.ruleForm.shouji&&(!this.$validate.isMobile(this.ruleForm.shouji))){
					this.$utils.msg(`手机应输入手机格式`);
					return
				}
				await this.$api.register(`${this.tableName}`, this.ruleForm, this.emailcode);
				this.$utils.msgBack('注册成功');;
			}
		}
	}
</script>

<style lang="scss" scoped>
	$color-primary: #b49950;

	.content {
		padding: 100upx;
	}
	
	.content:after {
		position: fixed;
		top: 0;
		right: 0;
		left: 0;
		bottom: 0;
		content: '';
				background-attachment: fixed;
		background-size: cover;
		background-position: center;
	}

	.logo {
		text-align: center;

		image {
			height: 200upx;
			width: 200upx;
			margin: 0 0 60upx;
		}
	}

	.uni-form-item {
		margin-bottom: 40upx;
		padding: 0;

		.uni-input {
			font-size: 30upx;
			padding: 7px 0;
		}
	}

	button[type="primary"] {
		background-color: $color-primary;
		border-radius: 0;
		font-size: 34upx;
		margin-top: 60upx;
	}

	.links {
		text-align: center;
		margin-top: 40upx;
		font-size: 26upx;
		color: #999;

		view {
			display: inline-block;
			vertical-align: top;
			margin: 0 10upx;
		}

		.link-highlight {
			color: $color-primary
		}
	}
.picker-select-input {
	line-height: 60rpx;
}

</style>
