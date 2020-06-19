基于  `puppeteer+typescript+jest` 的 `UI` 自动化测试     
#### 一、测试内容     
这是对百度进行测试的一个小例子。测试包括对百度标题和搜索到的内容进行断言     
#### 二、文件意义   
##### （1）配置文件    
`jest.config.js` 为 `jest` 的配置文件     
`jest.setup.js` 设置 `jest`  发起回调的超时时间   
`package.json` 由 `npm init` 生成，记载了需要的各种包和依赖，可通过 `npm install` 安装    
`puppeteer_environmnet.js` 测试环境    
`tsconfig.json` 为 `typescript` 的配置文件    
##### （2）测试用例   
文件名后缀包含 `.test.` 的文件，如 `search.test.ts`   
##### （3）方法 
`actions` 目录下的文件，如 `search.ts`       
