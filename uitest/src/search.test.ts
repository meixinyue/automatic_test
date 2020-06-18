import {searchAction} from './actions/search'
import {Page, launch} from 'puppeteer'
import config from './config'
import expectPuppeteer = require('expect-puppeteer');

const puppeteer = require('puppeteer')
describe('百度搜索',()=>{
    let page:Page;
    beforeEach(async () =>{
        const broswer = await puppeteer.launch({headless:false})
        page = await broswer.newPage()
        await page.goto(config.url)
    })
    afterEach(async () =>{
        await page.close()
    })

    test('Test-001:页面标题',async()=>{
        const pageTitle = await page.$eval('title', elem => {
            return elem.innerHTML;
        });
        await expect(pageTitle).toMatch('百度');
    })

    test('Test:002: 搜索内容'　,async() =>{
        let searchaction = new searchAction();
        await searchaction.searchinfo(page,'博客');

        await page.waitFor(2000);
        
        const result = await page.$eval('em',elem =>{
            return elem.innerHTML;
        })
        await expect(result).toMatch('博客');

    })
})