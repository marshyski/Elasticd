from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

resource_locator = None
registrar = None


def start(_registrar, _locator, config):
    ''' Start AP jobs with interval defined in settings.cfg '''
    global resource_locator, registrar
    locate_interval = config.getint('DEFAULT', 'locate_interval')
    driver_interval = config.getint('DEFAULT', 'driver_interval')
    resource_locator = _locator
    registrar = _registrar
    scheduler.add_job(process_locator, 'interval', seconds=locate_interval)
    scheduler.add_job(process_registrar, 'interval', seconds=driver_interval)
    scheduler.print_jobs()
    ''' THIS WILL NOT RETURN '''
    scheduler.start()


def process_locator():
    resources = resource_locator.get_resources()
    for item in resources:
        print 'register {0}'.format(item)
        registrar.register(item)


def process_registrar():
    registrar.process()
