# account.UploadWallPaper

Create and upload a new wallpaper



## Example

::::tabs
:::tab{title="JavaScript"}
```js
const {Api, TelegramClient} = require('telegram');
const {StringSession} = require('telegram/sessions');

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result = await client.invoke(new Api.account.UploadWallPaper({
    file: client.uploadFile('/path/to/file.jpg'),
    mimeType: 'some string here',
    settings: new Api.WallPaperSettings({
        blur: true,
        motion: true,
        backgroundColor: 43,
        secondBackgroundColor: 43,
        intensity: 43,
        rotation: 43
    })
}));
    console.log(result); // prints the result
})();
```
:::

:::tab{title="TypeScript"}
```ts
import {Api, TelegramClient} from 'telegram';
import {StringSession} from 'telegram/sessions';

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result: Api.WallPaper = await client.invoke(new Api.account.UploadWallPaper({
    file: client.uploadFile('/path/to/file.jpg'),
    mimeType: 'some string here',
    settings: new Api.WallPaperSettings({
        blur: true,
        motion: true,
        backgroundColor: 43,
        secondBackgroundColor: 43,
        intensity: 43,
        rotation: 43
    })
}));
    console.log(result); // prints the result
})();
```
:::
::::



## Parameters

| Name | Type | Description |
| :--: | ---- | ----------- |
| **file** | [InputFile](https://core.telegram.org/type/InputFile) | The JPG/PNG wallpaper 
| **mimeType** | [string](https://core.telegram.org/type/string) | MIME type of uploaded wallpaper 
| **settings** | [WallPaperSettings](https://core.telegram.org/type/WallPaperSettings) | Wallpaper settings 


## Result

[WallPaper](https://core.telegram.org/type/WallPaper)



## Possible errors

| Code | Type | Description |
| :--: | ---- | ----------- |


## Can bots use this method?

Yes

## Related pages

