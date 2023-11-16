import sentry_sdk

sentry_sdk.init(
    dsn="https://d463da0b5af9be72ed2cb06066bd6d21@o4506223878537216.ingest.sentry.io/4506234346340352",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    environment="development",
    # traces_sample_rate=1.0,
    
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.

    # profiles_sample_rate=1.0,

    release='1.0'
)

if __name__ == "__main__":
    devizion_zero = 1/0