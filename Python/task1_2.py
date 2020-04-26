def parse_cookie(query):
	dict_query= {}
	if len(query) == False:
		return dict_query
	first_split=query.split(';')

	for i in range(len(first_split)):
		if len(first_split[i]) >0:
			index=first_split[i].find('=')
			if index>0:
				dict_query[first_split[i][:index ]]=first_split[i][index+1:]
			else:
				dict_query[first_split[i]]=''
		else:
			break
			
	return dict_query

if __name__ == '__main__':
	assert parse_cookie('name=Dima;') == {'name': 'Dima'}
	assert parse_cookie('') == {}
	assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
	assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
	assert parse_cookie('name=Dima;age=28;path=/') == {'name': 'Dima', 'age': '28', 'path': '/'}
	assert parse_cookie('name=Dima;age=28;path=/;expires=Tue, 19 Jan 2038 03:14:07 GMT') == {'name': 'Dima', 'age': '28', 'path': '/', 'expires': 'Tue, 19 Jan 2038 03:14:07 GMT'}
	assert parse_cookie('name=Dima;age=28;;') == {'name': 'Dima', 'age': '28'}
	assert parse_cookie('name=Dima;age=28;domain=site.com') == {'name': 'Dima', 'age': '28','domain': 'site.com' }
	assert parse_cookie('name=Dima;age=28;secure') == {'name': 'Dima', 'age': '28', 'secure' : ''}
	assert parse_cookie('name=Dima;age=28;max-age=3600') == {'name': 'Dima', 'age': '28', 'max-age': '3600'}
