def parse(query):
	dict_query = {}
	first_split=query.split('?')
	if len(first_split)>1:
		second_split=first_split[1].split('&')
		for i in second_split:
			if len(i)>0:
				key_value=i.split('=')
				dict_query[key_value[0]]=key_value[1]
	return dict_query

if __name__ == '__main__':
	assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
	assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
	assert parse('http://example.com/') == {}
	assert parse('http://example.com/?') == {}
	assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
	assert parse('http://example.com/?name=') == {'name': ''}
	assert parse('http://example.com/?name=Dima&color=red&RGB=1064') == {'name': 'Dima', 'color': 'red', 'RGB': '1064'}
	assert parse('http://example.com/?name=Dima&color=') == {'name': 'Dima', 'color': ''}
	assert parse('http://example.com/?name=Dima&&') == {'name': 'Dima'}
	assert parse('http://example.com/?name=Dima&pin=****') == {'name': 'Dima', 'pin': '****'}
	assert parse('http://example.com/?&') == {}