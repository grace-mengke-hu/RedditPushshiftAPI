def date_utc_dic(date):
    '''
    date: string format of date and time
    '''
    date_utc = {
        'Wednesday, January 1, 2020 12:00:00 AM':1577836800,
        'Friday, January 31, 2020 11:59:59 PM':1580515199,
        'Saturday, February 1, 2020 12:00:00 AM': 1580515200,
        'Saturday, February 29, 2020 11:59:59 PM':1583020799,
         'Sunday, March 1, 2020 12:00:00 AM':1583020800,
         'Tuesday, March 31, 2020 11:59:59 PM':1585699199,
         'Wednesday, April 1, 2020 12:00:00 AM':1585699200,
         'Thursday, April 30, 2020 11:59:59 PM':1588291199,
         'Friday, May 1, 2020 12:00:00 AM':1588291200,
         'Sunday, May 31, 2020 11:59:59 PM':1590969599,
         'Monday, June 1, 2020 12:00:00 AM':1590969600,
          'Tuesday, June 30, 2020 11:59:59 PM':1593561599,
          'Wednesday, July 1, 2020 12:00:00 AM':1593561600,
         'Friday, July 31, 2020 11:59:59 PM':1596239999,
         'Saturday, August 1, 2020 12:00:00 AM':1596240000,
         'Monday, August 31, 2020 11:59:59 PM':1598918399,
         'Tuesday, September 1, 2020 12:00:00 AM':1598918400,
         'Wednesday, September 30, 2020 11:59:59 PM':1601510399,
         'Thursday, October 1, 2020 12:00:00 AM':1601510400,
          'Saturday, October 31, 2020 11:59:59 PM':1604188799,
          'Sunday, November 1, 2020 12:00:00 AM':1604188800,
          'Monday, November 30, 2020 11:59:59 PM':1606780799,
          'Tuesday, December 1, 2020 12:00:00 AM':1606780800,
          'Thursday, December 31, 2020 11:59:59 PM':1609459199    
        }
    return date_utc[date]

