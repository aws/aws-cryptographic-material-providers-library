// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

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

static mut COUNTER: usize = 0;
static mut TOTAL: usize = 0;

fn add_to_counter(inc: usize) {
    // SAFETY: There are no other threads which could be accessing `COUNTER`.
    unsafe {
        COUNTER += 1;
        TOTAL += inc;
    }
}

fn get_counter() -> usize {
    // SAFETY: There are no other threads which could be accessing `COUNTER`.
    unsafe { COUNTER }
}

fn get_total() -> usize {
    // SAFETY: There are no other threads which could be accessing `COUNTER`.
    unsafe { TOTAL }
}

use std::alloc::{GlobalAlloc, Layout, System};

struct MyAllocator;

unsafe impl GlobalAlloc for MyAllocator {
    unsafe fn alloc(&self, layout: Layout) -> *mut u8 {
        add_to_counter(layout.size());
        System.alloc(layout)
    }

    unsafe fn dealloc(&self, ptr: *mut u8, layout: Layout) {
        System.dealloc(ptr, layout)
    }
}

#[global_allocator]
static GLOBAL: MyAllocator = MyAllocator;
