// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

use std::sync::atomic::AtomicUsize;
use std::sync::atomic::Ordering;

pub struct ResourceTracker {
    count: usize,
    total: usize,
    time: std::time::SystemTime,
    cpu: cpu_time::ProcessTime,
}

impl ResourceTracker {
    pub fn new() -> Self {
        Self {
            count: get_counter(),
            total: get_total(),
            time: std::time::SystemTime::now(),
            cpu: cpu_time::ProcessTime::now(),
        }
    }
    pub fn report_leak(&self) {
        println!("{} outstanding allocations totalling {} bytes.", get_net_counter(), get_net_total());
    }
    pub fn report(&self) {
        let time = self.time.elapsed().unwrap().as_secs_f64();
        let cpu = self.cpu.elapsed().as_secs_f64();
        println!(
            "Allocation Count : {}, Total : {}, CPU Time : {}, Clock Time : {}",
            get_counter() - self.count,
            get_total() - self.total,
            cpu,
            time
        );
    }
}

static COUNTER: AtomicUsize = AtomicUsize::new(0);
static TOTAL: AtomicUsize = AtomicUsize::new(0);

static NET_COUNTER: AtomicUsize = AtomicUsize::new(0);
static NET_TOTAL: AtomicUsize = AtomicUsize::new(0);

fn add_to_counter(inc: usize) {
    COUNTER.fetch_add(1, Ordering::SeqCst);
    TOTAL.fetch_add(inc, Ordering::SeqCst);
    NET_COUNTER.fetch_add(1, Ordering::SeqCst);
    NET_TOTAL.fetch_add(inc, Ordering::SeqCst);
}

fn subtract_from_counter(inc: usize) {
    NET_COUNTER.fetch_sub(1, Ordering::SeqCst);
    NET_TOTAL.fetch_sub(inc, Ordering::SeqCst);
}

fn get_counter() -> usize {
    COUNTER.load(Ordering::SeqCst);
}

fn get_total() -> usize {
    TOTAL.load(Ordering::SeqCst);
}

fn get_net_counter() -> usize {
    NET_COUNTER.load(Ordering::SeqCst);
}

fn get_net_total() -> usize {
    NET_TOTAL.load(Ordering::SeqCst);
}

use std::alloc::{GlobalAlloc, Layout, System};

struct MyAllocator;

unsafe impl GlobalAlloc for MyAllocator {
    unsafe fn alloc(&self, layout: Layout) -> *mut u8 {
        add_to_counter(layout.size());
        System.alloc(layout)
    }

    unsafe fn dealloc(&self, ptr: *mut u8, layout: Layout) {
        subtract_from_counter(layout.size());
        System.dealloc(ptr, layout)
    }
}

#[global_allocator]
static GLOBAL: MyAllocator = MyAllocator;
