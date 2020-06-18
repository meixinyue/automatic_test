import {Page} from 'puppeteer';

export class searchAction{
    public async searchinfo(page:Page, information:string){
        const search_Input = await page.waitForSelector('#kw');
        await search_Input.type(information);

        const search_Btn = await page.waitForSelector('.bg.s_btn');
        await search_Btn.click();
    }
}