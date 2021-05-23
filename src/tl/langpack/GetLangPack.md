# langpack.GetLangPack

Get localization pack strings



## Example

::::tabs
:::tab{title="JavaScript"}
```js
const {Api, TelegramClient} = require('telegram');
const {StringSession} = require('telegram/sessions');

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result = await client.invoke(new Api.langpack.GetLangPack({
    langPack: 'some string here',
    langCode: 'some string here'
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
    const result: Api.LangPackDifference = await client.invoke(new Api.langpack.GetLangPack({
    langPack: 'some string here',
    langCode: 'some string here'
}));
    console.log(result); // prints the result
})();
```
:::
::::



## Parameters

| Name | Type | Description |
| :--: | ---- | ----------- |
| **langPack** | [string](https://core.telegram.org/type/string) | Language pack name 
| **langCode** | [string](https://core.telegram.org/type/string) | Language code 


## Result

[LangPackDifference](https://core.telegram.org/type/LangPackDifference)



## Possible errors

| Code | Type | Description |
| :--: | ---- | ----------- |
| 400 | LANG\_PACK\_INVALID | The provided language pack is invalid 


## Can bots use this method?

Yes

## Related pages

