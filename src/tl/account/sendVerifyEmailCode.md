# account.sendVerifyEmailCode

Send the verification email code for telegram [passport](https://core.telegram.org/passport).

## Example

::::tabs
:::tab{title="JavaScript"}

```js
const { Api, TelegramClient } = require('telegram');
const { StringSession } = require('telegram/sessions');

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result = await client.invoke(
        new Api.account.sendVerifyEmailCode({
            email: 'random string here',
        }),
    );
    console.log(result); // prints the result
})();
```

:::

:::tab{title="TypeScript"}

```ts
import { Api, TelegramClient } from 'telegram';
import { StringSession } from 'telegram/sessions';

const session = new StringSession('');
const client = new TelegramClient(session, apiId, apiHash, {});

(async function run() {
    const result: Api.account.SentEmailCode = await client.invoke(
        new Api.account.sendVerifyEmailCode({
            email: 'random string here',
        }),
    );
    console.log(result); // prints the result
})();
```

:::
::::

## TL schema

```txt
account.sentEmailCode#811f854f email_pattern:string length:int = account.SentEmailCode;
---functions---
account.sendVerifyEmailCode#7011509f email:string = account.SentEmailCode;
```

## Parameters

|   Name    | Type                                            | Description                      |
| :-------: | ----------------------------------------------- | -------------------------------- |
| **email** | [string](https://core.telegram.org/type/string) | The email where to send the code |

## Result

[account.SentEmailCode](https://core.telegram.org/type/account.SentEmailCode)

## Possible errors

| Code | Type | Description |
| :--: | ---- | ----------- |

## Can bots use this method?

Yes

## Related pages

### [Telegram Passport Manual](https://core.telegram.org/passport)