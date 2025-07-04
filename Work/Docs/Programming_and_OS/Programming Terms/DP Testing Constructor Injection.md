---
summary: Dependencies are provided through a client's class constructor, meaning you cannot create a new instance of the class without passing in a variable of the type required by the constructor. Make sure to avoid the possibility of passing in a null parameter.
implements: ["[[DP guard pattern]]"]
source: ["[[DP Testing Dependency Injection]]"]
date created: Wednesday, November 6th 2024, 9:32:48 am
date modified: Wednesday, November 6th 2024, 9:47:42 am
type: note/concept
---
`VIEW[**{summary}**][text(renderMarkdown)]`

# Usage
```cpp
class BankingService {}

class PayrollSystem {
	private _BankingService: BankingService;

	constructor(aBankingService: BankingService)
	{
		if (!aBankingService)
		{
			throw new Error('Do not allow null')
		}
		this._BankingService = aBankingService;
	}
}
```