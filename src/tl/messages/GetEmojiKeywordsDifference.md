# messages.GetEmojiKeywordsDifference

Get changed emoji keywords



## Example

::::tabs
:::tab{title="JavaScript"}
```js
const {Api, TelegramClient} = require('telegram');
const {StringSession} = require('telegram/sessions');

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result = await client.invoke(new Api.messages.GetEmojiKeywordsDifference({
    langCode: 'some string here',
    fromVersion: 43
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
    const result: Api.EmojiKeywordsDifference = await client.invoke(new Api.messages.GetEmojiKeywordsDifference({
    langCode: 'some string here',
    fromVersion: 43
}));
    console.log(result); // prints the result
})();
```
:::
::::



## Parameters

| Name | Type | Description |
| :--: | ---- | ----------- |
| **langCode** | [string](https://core.telegram.org/type/string) | Language code 
| **fromVersion** | [int](https://core.telegram.org/type/int) | Previous emoji keyword localization version 


## Result

[EmojiKeywordsDifference](https://core.telegram.org/type/EmojiKeywordsDifference)



## Possible errors

| Code | Type | Description |
| :--: | ---- | ----------- |


## Can bots use this method?

Yes

## Related pages

