from django.shortcuts import render
import requests
import pandas as pd
# Create your views here.

def IndexPage(request):
    data_state_table = getStateDataByTable("https://api.covid19india.org/data.json")
    data_india_active = india_active('https://api.covid19india.org/csv/latest/case_time_series.csv')
    data_india_recovered = india_recovered('https://api.covid19india.org/csv/latest/case_time_series.csv')
    data_india_deaths = india_deaths('https://api.covid19india.org/csv/latest/case_time_series.csv')
    data_india = get_total_india('https://api.covid19india.org/csv/latest/case_time_series.csv')
    data_india['active'] = data_india['confirm'] - (data_india['recover'] + data_india['death'])
    return render(request,'index.html',{"state_table":data_state_table,"data_india":data_india,'data_india_active':data_india_active,'data_india_recovered':data_india_recovered,'data_india_deaths':data_india_deaths})
    
def PreddictionPage(request):
    data_state_table = getStateDataByTable("https://api.covid19india.org/data.json")
    data_india_active = india_active('https://api.covid19india.org/csv/latest/case_time_series.csv')
    data_india_recovered = india_recovered('https://api.covid19india.org/csv/latest/case_time_series.csv')
    data_india_deaths = india_deaths('https://api.covid19india.org/csv/latest/case_time_series.csv')
    data_india = get_total_india('https://api.covid19india.org/csv/latest/case_time_series.csv')
    data_india['active'] = data_india['confirm'] - (data_india['recover'] + data_india['death'])
    return render(request,'predict.html',{"state_table":data_state_table,"data_india":data_india,'data_india_active':data_india_active,'data_india_recovered':data_india_recovered,'data_india_deaths':data_india_deaths})

def SubscriptionPage(request):
    return render(request,'subscription.html',{})

def DataTablePage(request):
    return render(request,'datatable.html',{})

def MapPage(request):
    state = getStateDataWithStateCode("https://api.covid19india.org/data.json")
    ans = "active"
    passing = []
    for i in state:
        temp = {}
        temp['id'] = i['code']
        temp['name'] = i['state_name']
        temp['value'] = i[ans]
        passing.append(temp)
    if request.method == "POST":
        print(1)
        ans = request.POST.get('check')
        print(ans)
        passing = []
        for i in state:
            temp = {}
            temp['id'] = i['code']
            temp['name'] = i['state_name']
            temp['value'] = i[ans]
            passing.append(temp)
        return render(request,"map.html",{'State':passing,'ans':ans})
    return render(request,"map.html",{'State':passing,'ans':ans})    

# State Map Data 
def getStateDataWithStateCode(url):
    response = requests.get(url)
    data = response.json()
    state_data_with_code = []
    for state in (data['statewise']):
        if state['state'] == 'Total' or state['state'] == 'State Unassigned':
            pass
        else:
            temp = {}
            temp['state_name']= state['state']
            temp['code'] ="IN." + state['statecode'].upper()
            temp['active']= state['active']
            temp['confirmed'] = state['confirmed']
            temp['deaths'] = state['deaths']
            temp['recovered']= state['recovered']
            state_data_with_code.append(temp)
    return state_data_with_code

#State Data As Table
def getStateDataByTable(url):
    response = requests.get(url)
    data = response.json()
    state_data_table = []
    count=1
    for state in (data['statewise']):
        if state['state'] == 'Total' or state['state'] == 'State Unassigned':
            pass
        else:
            lst = [count,state['state'],state['confirmed'],state['active'],state['recovered'],state['deaths']]
            state_data_table.append(lst)
            count += 1
    return state_data_table

#India Total Data Value
def get_total_india(url):
    df = pd.read_csv(url)
    #    print(df[['Date',"Daily Recovered"]].tail(6))
    india_c = list(df['Total Confirmed'])
    india_d = list(df['Total Deceased'])
    india_r = list(df['Total Recovered'])

    return {'confirm': india_c[-1], 'death': india_d[-1],'recover':india_r[-1]}

#India Chart Value

def india_active(url):
    df = pd.read_csv(url)
    #    print(df[['Date',"Daily Confirmed"]].tail(6))
    india_date = list(df['Date'])
    india_confirmed_cases = list(df['Daily Confirmed'])

    return {'date': india_date, 'active': india_confirmed_cases}

def india_recovered(url):
    df = pd.read_csv(url)
    #    print(df[['Date',"Daily Recovered"]].tail(6))
    india_date = list(df['Date'])
    india_confirmed_cases = list(df['Daily Recovered'])

    return {'date': india_date, 'recovered': india_confirmed_cases}
def india_deaths(url):
    df = pd.read_csv(url)
    #    print(df[['Date',"Daily Recovered"]].tail(6))
    india_date = list(df['Date'])
    india_confirmed_cases = list(df['Daily Deceased'])

    return {'date': india_date, 'death': india_confirmed_cases} 